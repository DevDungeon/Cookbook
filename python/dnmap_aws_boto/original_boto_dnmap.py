#!/usr/bin/env python
from datetime import datetime, date, time
import time
import boto3
import sys
import os.path

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
client2 = boto3.client('ecs')

#Counts the number of scan files to see if it matches the number of lines in the dnmapcommands file
def dnmapserverwatch():
    path = os.getenv('HOME') + '/dnmap_v0.6/nmap_results'
    num_files = 0
    num_lines = sum(1 for line in open(os.getenv('HOME') + '/dnmapcommands'))
    while int(num_files) != int(num_lines):
        num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
        print 'Scanning Targets....' + str(num_files) + ' scans complete.'
        time.sleep(45)
    print 'Scans are finished.'

#terminates spot instances with the ECS profile
def terminatespots():
    response = client.describe_instances(

        Filters=[
            {
                'Name': 'iam-instance-profile.arn',
                    'Values': [
                        'arn:aws:iam::106842908066:instance-profile/ecsInstanceRole',
                    ]
            },
        ],
    )


    instanceIds = []
    for s in response['Reservations']:
        for f in s['Instances']:
            instanceIds.append(f['InstanceId'])
    reponse2 = client.terminate_instances(

        InstanceIds= instanceIds
    
    )
    print 'Terminating Spots.'
#deploys containers with command overrides
def deploycontainers(containernumber):
    response = client2.run_task(
        cluster='default',
        taskDefinition='DnmapClients:18',
        overrides={
            'containerOverrides': [
                {
                    'name':'DnmapClients',
                    'command':[
                        '/bin/bash','-c','dnmap_client -s ' + sys.argv[2],
                    ],
                },
            ]
        },
        count=int(containernumber)
    )

#checks to see how many spots are in the ECS cluster
def clustercheck():
    response = client2.describe_clusters(
        clusters=[
            'default',
        ]
    )
    return response['clusters'][0]['registeredContainerInstancesCount']

#counts the number of active spots you have
def spotinstancestatuscheck():
    response = client.describe_spot_instance_requests(

        Filters=[
            {
                'Name': 'state',
                'Values': [
                    'open','active','failed',
                ]
            },
        ]
    )
    instancehealth = []
    for s in response['SpotInstanceRequests']:
        instancehealth.append(s['State'])
    return instancehealth.count('active')
    
#turns up the number of spot instances you specified
def instanceturnup(zone):
    response = client.request_spot_instances(
        #You want to actually start an instance so no dryrun!
        DryRun=False,
        #This is the max spot price you are willing to pay.  Check spot prices through the gui (or programatically when you get fancy).  You'll pay the current spot price and the instance will stop when you go over this number.
        SpotPrice='.03',
        #Number of instances you want to turn up with this configuration
        InstanceCount= int(sys.argv[1]),
        #Is this a one-time thing or do you want this request to be persistent.  I believe if you choose persistent it will come back once spot price goes below your selected price
        Type='one-time',
        LaunchSpecification={
            #This is the image ID for ubuntu 14.04 64bit.  You can find other imageIDs on the aws marketplace.  Most are free.
            'ImageId': 'ami-b540eade',
            #The public/private key pair to install on this server.  You need to create this before hand.
            'KeyName': 'newsoft',
            #What size instance you want. Remember to check spot price on the size of instance you want.  Spot price also changes with what availability zone you want which you can specify below.
            'InstanceType': 'm3.medium',
            #What availability zone do you want?
            'Placement': {
                'AvailabilityZone': zone,
            },
            #This is the elastic block storage config
            'BlockDeviceMappings': [
                {
                    #Device name to use when it attaches to the instance.  /dev/sda1 is reserved for root I believe.
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
                    #The network interface's position in the attachment order.  You'll only need one.
                    'DeviceIndex': 0,
                    'Groups': [
                        #What security group should you use?  You'll need to create ahead of time and it's the security group ID not the group name
                        'sg-10385b77',
                    ],
                    #Usually you'll want your instance to have an associated public ID so you can ssh into it if needed.  Obviously you'll restrict who can access it and how through your security group.
                    'AssociatePublicIpAddress': True
                },
            ],
            'IamInstanceProfile': {
                'Arn': 'arn:aws:iam::106842908066:instance-profile/ecsInstanceRole',
                #'Name': 'arn:aws:iam::106842908066:role/ecsInstanceRole'
            },
            #If you want cloudwatch monitoring.  I have this off for now as it's free to a point.
            'Monitoring': {
                'Enabled': False
            },

        }
    )

#checks the spot prices and then returns the region with the lowest price
def checkprice():
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
                    'us-east-1a','us-east-1b','us-east-1c','us-east-1e',
                ]
            },
        ],

        MaxResults=1000,

    )
    prices = [response['SpotPriceHistory'][0]['SpotPrice'],response['SpotPriceHistory'][1]['SpotPrice'],response['SpotPriceHistory'][2]['SpotPrice'],response['SpotPriceHistory'][3]['SpotPrice']]
    minprice = min(prices)
    slot = prices.index(minprice)
    lowestpricezone = response['SpotPriceHistory'][slot]['AvailabilityZone']

    print '----Zone Prices------------------------------------------------------------------'
    print (response['SpotPriceHistory'][0]['SpotPrice'], response['SpotPriceHistory'][0]['AvailabilityZone'])
    print (response['SpotPriceHistory'][1]['SpotPrice'], response['SpotPriceHistory'][1]['AvailabilityZone'])
    print (response['SpotPriceHistory'][2]['SpotPrice'], response['SpotPriceHistory'][2]['AvailabilityZone'])
    print (response['SpotPriceHistory'][3]['SpotPrice'], response['SpotPriceHistory'][3]['AvailabilityZone'])
    print '---------------------------------------------------------------------------------'
    print lowestpricezone + ' is the lowest priced zone.  Turning up ' + sys.argv[1] + ' spot instances in ' + lowestpricezone 
    return lowestpricezone

def main():
    Azone = checkprice()
    #turn up instances in the lowest price zone
    instanceturnup(zone=Azone)
    #loop checking to see when the spot instances are active
    while spotinstancestatuscheck() != int(sys.argv[1]):
        spotsup = spotinstancestatuscheck()
        spotstogo = int(sys.argv[1]) - spotsup
        print 'Not all of your instances are up.'
        print str(spotsup) + ' are up. ' + str(spotstogo) + ' spots to go.' 
        time.sleep(15)
    if spotinstancestatuscheck() == int(sys.argv[1]):
        #loop that checking your ECS cluster size
        while clustercheck() != int(sys.argv[1]):
            ecsinstances = clustercheck()
            ecstogo = int(sys.argv[1]) - ecsinstances
            print 'Not all of your instances are registered with ECS yet.'
            print str(ecsinstances) + ' are attached to the cluster. ' + str(ecstogo) + ' instaces to go.' 
            time.sleep(15)
        print 'All instances are now registered with ECS.  Deploying containers.'
        #You can only submit job requests 10 at a time so the code below finds out how many containers you specified and then requests over and over until your number is hit
        commandnumber = int(sys.argv[1])
        sumnumber = commandnumber / 10
        leftover = commandnumber - (sumnumber * 10)
        if commandnumber < 11:
            deploycontainers(commandnumber)
        else:
            n = sumnumber
            while (n > 0):
                deploycontainers(10)
                n = n - 1
            if (leftover > 0):
                deploycontainers(leftover)
        #Watches scan result folder to understand when scans are complete
        dnmapserverwatch()
        #terminates spots once scans are done
        terminatespots()
            
if __name__ == '__main__':
    main()
