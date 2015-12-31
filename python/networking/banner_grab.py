import socket


def getBanner(ip, port):
    try:
        socket.setdefaulttimeout(1)
        sock = socket.socket()
        sock.connect((ip, port))
        banner = sock.recv(1024)
        return banner
    except:
        return


def checkVulns(banner):
    print('Checking banners')
    for vuln_banner in open('vuln_banners.txt', 'r').readlines():
        print('Checking banner: ' + vuln_banner)
        if vuln_banner.strip('\n') in banner:
            print('[+] Vulnerability found: ' + vuln_banner)
    return


def main():
    portList = [21, 22, 25, 80, 110, 443]
    for x in range(1, 33):
        ip = '192.168.1.' + str(x)
        for port in portList:
            print('Checking: ' + str(ip) + ':' + str(port))
            banner = getBanner(ip, port)
            if banner:
                print('[+] ' + ip + ': ' + banner)
                checkVulns(banner)

if __name__ == '__main__':
    main()