from datetime import datetime
import time
import boto3
import sys
import os.path

max_instance_count = int(sys.argv[1])  # Do the cast to int once instead of every time you use it
dnmap_server_ip = sys.argv[2]
nmap_results_directory = '/dnmap_v0.6/nmap_results'

ec2 = boto3.resource('ec2')
# These names could be a little more descriptive. Are they  doing the same thing? they could go in an array
# so you can just append and remove clients on the fly
client = boto3.client('ec2')
client2 = boto3.client('ecs')


def dnmap_server_watch():
    """
    Counts the number of scan files to see if it matches the number of lines in the dnmapcommands file
    """
    path = os.getenv('HOME') + nmap_results_directory
    num_files = 0
    num_lines = sum(1 for line in open(os.getenv('HOME') + '/dnmapcommands'))
    while int(num_files) != int(num_lines):
        num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
        print 'Scanning targets....' + str(num_files) + ' scans complete.'
        time.sleep(45)
    print 'Scans are finished.'


def terminate_all_spots():
    """
    Terminate spot instances with the ECS profile
    """
    response = client.describe_instances(
        Filters=[
            {
                'Name': 'iam-instance-profile.arn',
                'Values': ['arn:aws:iam::106842908066:instance-profile/ecsInstanceRole']
            },
        ],
    )
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    print 'Terminating Spots.'
    client.terminate_instances(InstanceIds=instance_ids)


def deploy_containers(num_containers):
    """
    Deploy containers with command overrides
    """
    client2.run_task(
        cluster='default',
        taskDefinition='DnmapClients:18',
        overrides={
            'containerOverrides': [
                {
                    'name': 'DnmapClients',
                    'command': [
                        '/bin/bash', '-c', 'dnmap_client -s ' + dnmap_server_ip,
                    ],
                },
            ]
        },
        count=int(num_containers)
    )


def deploy_all_containers(num_containers):
    """
    Deploy containers, 10 at a time (Amazon limit)
    """
    quotient = num_containers / 10
    remainder = num_containers - (quotient * 10)

    if num_containers < 11:
        deploy_containers(num_containers)
    else:
        runs_left = quotient
        while runs_left > 0:
            deploy_containers(10)
            runs_left -= 1
        if remainder > 0:
            deploy_containers(remainder)


def num_registered_instances():
    """
    How many instances are in the ECS cluster
    """
    response = client2.describe_clusters(clusters=['default'])
    return response['clusters'][0]['registeredContainerInstancesCount']


def active_spot_count():
    """
    Number of active spots you have
    """
    response = client.describe_spot_instance_requests(
        Filters=[
            {
                'Name': 'state',
                'Values': [
                    'open',
                    'active',  # You can probably filter it by only active to get only active
                    'failed',
                ]
            },
        ]
    )
    # If you filter it by just active you can probably skip this and just get the count of the
    # response['SpotInstanceRequests'] instances since the only ones returned will be active.
    instance_health = []
    for s in response['SpotInstanceRequests']:
        instance_health.append(s['State'])
    return instance_health.count('active')


def turn_up_instance(zone):
    """
    Turn up the specified number of spot instances
    """
    client.request_spot_instances(
        DryRun=False,
        SpotPrice='.03',  # If price surpasses this limit, instance will stop
        InstanceCount=max_instance_count,
        # one-time|persistent - I believe persistent will come back once spot price goes below selected price
        Type='one-time',
        LaunchSpecification={
            # Ubuntu 14.04 64-bit. More free images on AWS marketplace
            'ImageId': 'ami-b540eade',
            # The public/private key pair to install on this server.  You need to create this before hand.
            'KeyName': 'newsoft',
            # What size instance you want. Remember to check spot price on the size of instance you want.
            # Spot price also changes with what availability zone you want which you can specify below.
            'InstanceType': 'm3.medium',
            'Placement': {
                'AvailabilityZone': zone,
            },
            # Elastic block storage config
            'BlockDeviceMappings': [
                {
                    # Device name to use when it attaches to the instance.  /dev/sda1 is reserved for root I believe.
                    'DeviceName': '/dev/xvda',
                    'Ebs': {
                        'VolumeSize': 30,
                        'DeleteOnTermination': True,
                        'VolumeType': 'gp2',
                        'Encrypted': False
                    },
                },
            ],
            'NetworkInterfaces': [
                {
                    # The network interface's position in the attachment order.  You'll only need one.
                    'DeviceIndex': 0,
                    'Groups': [
                        # Security group - Create ahead of time and it's the security group ID not the group name
                        'sg-10385b77',
                    ],
                    # Usually you'll want your instance to have an associated public ID so you can ssh into it if needed
                    # Obviously you'll restrict who can access it and how through your security group.
                    'AssociatePublicIpAddress': True
                },
            ],
            'IamInstanceProfile': {
                'Arn': 'arn:aws:iam::106842908066:instance-profile/ecsInstanceRole',
                # 'Name': 'arn:aws:iam::106842908066:role/ecsInstanceRole'
            },
            # If you want cloudwatch monitoring.  I have this off for now as it's free to a point.
            'Monitoring': {
                'Enabled': False
            },
        }
    )


def get_cheapest_spot_zone():
    """
    Get the lowest priced region/zone
    """
    response = client.describe_spot_price_history(
        StartTime=datetime.utcnow(),
        EndTime=datetime.utcnow(),
        InstanceTypes=[
            'm3.medium',
        ],
        ProductDescriptions=[
            'Linux/UNIX',
        ],
        Filters=[
            {
                'Name': 'availability-zone',
                'Values': [
                    'us-east-1a',
                    'us-east-1b',
                    'us-east-1c',
                    'us-east-1e',
                ]
            },
        ],
        MaxResults=1000,
    )

    prices = [
        response['SpotPriceHistory'][0]['SpotPrice'],
        response['SpotPriceHistory'][1]['SpotPrice'],
        response['SpotPriceHistory'][2]['SpotPrice'],
        response['SpotPriceHistory'][3]['SpotPrice']
    ]
    min_price = min(prices)
    slot = prices.index(min_price)
    lowest_price_zone = response['SpotPriceHistory'][slot]['AvailabilityZone']
    print '---- Zone Prices --------------------------------------------------------------'
    print (response['SpotPriceHistory'][0]['SpotPrice'], response['SpotPriceHistory'][0]['AvailabilityZone'])
    print (response['SpotPriceHistory'][1]['SpotPrice'], response['SpotPriceHistory'][1]['AvailabilityZone'])
    print (response['SpotPriceHistory'][2]['SpotPrice'], response['SpotPriceHistory'][2]['AvailabilityZone'])
    print (response['SpotPriceHistory'][3]['SpotPrice'], response['SpotPriceHistory'][3]['AvailabilityZone'])
    print '-------------------------------------------------------------------------------'

    print lowest_price_zone + ' is the lowest priced zone.  Turning up ' + str(max_instance_count) +\
        ' spot instances in ' + lowest_price_zone
    return lowest_price_zone


def main():
    """
    Spin up the cheapest Amazon spot instances and perform distributed nmap scans
    """
    cheapest_zone = get_cheapest_spot_zone()
    turn_up_instance(zone=cheapest_zone)

    # Wait for spots to spin up
    while active_spot_count() != max_instance_count:
        num_active_spots = active_spot_count()
        spots_to_go = max_instance_count - num_active_spots
        print 'Not all of your instances are up.'
        print str(num_active_spots) + ' are up. ' + str(spots_to_go) + ' spots to go.'
        time.sleep(15)

    # Wait for instances to register
    while num_registered_instances() != max_instance_count:
        ecs_instances = num_registered_instances()
        instances_to_go = max_instance_count - ecs_instances
        print 'Not all of your instances are registered with ECS yet.'
        print str(ecs_instances) + ' are attached to the cluster. ' + str(instances_to_go) + ' instances to go.'
        time.sleep(15)

    print 'All instances are now registered with ECS. Deploying containers.'
    deploy_all_containers(max_instance_count)
    print 'Containers deployed.'

    dnmap_server_watch()  # Watches scan result folder to understand when scans are complete

    terminate_all_spots()


if __name__ == '__main__':
    main()
