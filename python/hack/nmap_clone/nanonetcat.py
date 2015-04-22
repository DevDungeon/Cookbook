#!/usr/bin/python2
import sys
import socket
import getopt
import threading
import subprocess

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


def usage():
    print "NanoNetCat, a netcat clone"
    print
    print "Usage: nnc.py -t target_host -p port"
    print "-l --listen               - listen instead of send"
    print "-e --execute=file_to_run  - execute file when connection is recieved"
    print "-c --command              - run input as a shell command"
    print "-u --upload=destination   - upload files and write to destination"
    print
    print "Examples:"
    print "nnc.py -t 192.168.1.2 -p 5555 -l -c"
    print "nnc.py -t 192.168.1.2 -p 5555 -l -u=c:\\target.exe"
    print "nnc.py -t 192.168.1.2 -p 5555 -l -e=\"cat /etc/passwd\""
    print "echo 'DEADBEEF' | ./nnc.py -t 192.168.1.2 -p 5555"


def client_sender(buffer):
    client = socket.socket()
    try:
        client.connect((target, port))
        if len(buffer):
            client.send(buffer)
        while True:
            recv_len = 1
            response = ""
            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data
                if recv_len < 4096:
                    break
            print response
            buffer = raw_input()
            buffer += "\n"
            client.send(buffer)
    except:
        print "[*] Exception! Exiting."
        client.close()




def run_command(command):
    command = command.rstrip()
    try:
        output = subprocess.check_output(command,stderr=subprocess.STDOUT, shell=True)
    except:
        output = "Failed to execute command.\r\n"
    return output


def client_handler(client_socket):
    global upload
    global execute
    global command

    # Check for upload
    if len(upload_destination):
        file_buffer = ""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            else:
                file_buffer += data

        try:
            fyle = open(upload_destination, 'wb')
            fyle.write(file_buffer)
            fyle.close()
            client_socket.send("Successfully saved file to %s\r\n" % upload_destination)
        except:
            client_socket.send("Failed to save file to %s\r\n" % upload_destination)

    # Check for command execute
    if len(execute):
        output = run_command(execute)
        client_socket.send(output)
    # Create command shell if requested
    if command:
        while True:
            # Prompt
            client_socket.send("NanoNetCat >>> ")
            cmd_buffer = ""
            while "\n" not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)
            response = run_command(cmd_buffer)
            client_socket.send(response)


def server_loop():
    global target
    if not len(target):
        target = "0.0.0.0"
        server = socket.socket()
        server.bind((target,port))
        server.listen(5)
        while True:
            client_socket, addr = server.accept()
            client_thread = threading.Thread(target=client_handler,args=(client_socket,))
            client_thread.start()

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    # Print usage if no arguments are provided
    if not len(sys.argv[1:]):
        usage()

    # Get the command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:",
                         ["help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print str(err)
        usage()

    # Handle command line options
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--command"):
            command = True
        elif o in ("-u", "--uppload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False, "Unhandled Option"

    # Sending
    if not listen and len(target) and port > 0:
        buffer = sys.stdin.read()
        client_sender(buffer)

    # Listening
    if listen:
        server_loop()


main()