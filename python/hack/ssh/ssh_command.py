#!/usr/bin/python2
import threading
import paramiko
import subprocess

def ssh_command(ip, user, passwd, command, port=22):
    client = paramiko.SSHClient()
    #client.load_host_keys('/home/nanodano/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd, port=port)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print ssh_session.recv(1024)
    return

ssh_command('199.231.187.114', 'dtron', 'secretsauce', 'id', 2202)