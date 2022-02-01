#!/usr/bin/env python3
"""
ssh-copy-id.py

Copy your SSH public key into a remote
host's `~/.ssh/authorized_keys` file.

pip install paramiko

Usage: ssh-copy-id.py <host> <username>
"""
from paramiko import SSHClient, AutoAddPolicy
import sys
import os
from getpass import getpass
client = SSHClient()
#client.load_system_host_keys()
#client.load_host_keys('~/.ssh/known_hosts')
#client.set_missing_host_key_policy(AutoAddPolicy())
client.set_missing_host_key_policy(AutoAddPolicy)
print(f'connecting to {sys.argv[1]} with {sys.argv[2]}')
client.connect(sys.argv[1], username=sys.argv[2], password=getpass())

with  open(os.path.join(os.path.expanduser('~'), '.ssh', 'id_rsa.pub')) as f:
    pubkey = f.read()
    print(f'pubkey: {pubkey}')
    cmd = f'echo "{pubkey}" >> ~/.ssh/authorized_keys'
    print(f'Command: {cmd}')
    stdin, stdout, stderr = client.exec_command(cmd)
    stdin.channel.shutdown_write()
    print(f'Return code: {stdout.channel.recv_exit_status()}')
    # Print output of command. Will wait for command to finish.
    print(f'STDOUT: {stdout.read().decode("utf8")}')
    print(f'STDERR: {stderr.read().decode("utf8")}')
    stdin.close()
    stdout.close()
    stderr.close()

client.close()
