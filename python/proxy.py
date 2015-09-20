#!/usr/bin/python2
import sys
import socket
import threading


def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((local_host, local_port))
    except:
        print "[!!] Failed to listen on %s:%d" % (local_host, local_port)
        print "[!!] Check for other listening sockets or correct permissions."
        sys.exit(0)

    print "[*] Listening on %s:%d" % (local_host, local_port)

    server.listen(5)

    while True:
        client_socket, addr = server.accept()
        print "[==>] Received incoming connection from %s:%d" % (addr[0], addr[1])
        proxy_thread = threading.Thread(
            target=proxy_handler,
            args=(client_socket, remote_host, remote_port, receive_first)
        ).start()

def main():
    if len(sys.argv[1:]) != 5:
        print "Usage: ./proxy.py localhost localport remotehost remoteport receive_first"
        print "Example: ./proxy.py 127.0.0.1 9000 10.12.132.1 22 True"
        sys.exit(0)
    local_host = sys.argv[1]
    local_port = int(sys.argv[2])
    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])
    receive_first = sys.argv[5]
    if "True" in receive_first:
        receive_first = True
    else:
        receive_first = False

    server_loop(local_host, local_port, remote_host, remote_port, receive_first)


def proxy_handler(client_socket, remote_host, remote_port, receive_first):
    remote_socket = socket.socket()
    remote_socket.connect((remote_host, remote_port))

    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)
        # Send to response hander
        remote_buffer = response_handler(remote_buffer)
        if len(remote_buffer):
            print "[<==] Sending %d bytes to localhost." % len(remote_buffer)
            client_socket.send(remote_buffer)

    while True:
        # Read from localhost then forward to remote
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            print "[==>] Received %d bytes from localhost." % len(local_buffer)
            hexdump(local_buffer)

            local_buffer = request_handler(local_buffer)
            remote_socket.send(local_buffer)
            print "[==>] Sent to %s:%d." % (remote_host, remote_port)

        # Receive back response
        remote_buffer = receive_from(remote_socket)
        if len(remote_buffer):
            print "[<==] Received %d bytes from %s:%d." % (len(remote_buffer), remote_host, remote_port)
            hexdump(remote_buffer)
            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)
            print "[<==] Sent to localhost."
        # If no more data on either side close connections
        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print "[*] No more data. Closing connections."
            break


# Pretty hex dumping
def hexdump(data, length=16):
    result = []
    digits = 4 if isinstance(data, unicode) else 2
    for i in xrange(0, len(data), length):
        d = data[i:i+length]
        hexa = b' '.join(["%0*X" % (digits, ord(x)) for x in d])
        text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.' for x in d])
        result.append( b"%04X %-*s %s" % (i, length*(digits + 1), hexa, text))
    print b'\n'.join(result)


def receive_from(sock):
    buffer = ""
    sock.settimeout(30)
    try:
        while True:
            data = sock.recv(4096)
            if not data:
                break
            buffer += data
    except:
        pass

    return buffer


# Modify requests
def request_handler(data):
    return data


# Modify responses
def response_handler(data):
    return data




main()