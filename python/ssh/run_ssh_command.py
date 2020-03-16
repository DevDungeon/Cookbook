from paramiko import SSHClient

# Connect
client = SSHClient()
client.load_system_host_keys()
client.connect('example.com', username='user', password='pass')

# Run a command (execute PHP interpreter)
stdin, stdout, stderr = client.exec_command('php')
print(type(stdin))  # <class 'paramiko.channel.ChannelStdinFile'>
print(type(stdout))  # <class 'paramiko.channel.ChannelFile'>
print(type(stderr))  # <class 'paramiko.channel.ChannelStderrFile'>

# Optionally, send data via STDIN, and shutdown when done
stdin.write('<?php echo "Hello!"; sleep(2); ?>')
stdin.channel.shutdown_write()

# Print output of command. Will wait for command to finish.
print(f'STDOUT: {stdout.read().decode("utf8")}')
print(f'STDERR: {stderr.read().decode("utf8")}')

# Get return code from command (0 is default for success)
print(f'Return code: {stdout.channel.recv_exit_status()}')

# Because they are file objects, they need to be closed
stdin.close()
stdout.close()
stderr.close()

# Close the client itself
client.close()