"""
Run with:
  python3 portscan2csv.py www.devdungeon.com scan_results.csv
"""
import concurrent
import csv
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from socket import socket

MAX_THREADS = 128
TIMEOUT_IN_SECONDS = 5.0


def print_usage():
    print("""
Usage:
  python3 portscan2csv.py <host> <output_file>
Examples:
  python3 portscan2csv.py www.devdungeon.com scan_results.csv
""")


def check_args():
    if len(sys.argv) < 3:
        print("[-] Not enough arguments received.")
        print_usage()
        sys.exit(1)


def tcp_connect(host_or_ip, port):
    sock = socket()
    sock.settimeout(TIMEOUT_IN_SECONDS)
    try:
        sock.connect((host_or_ip, port))
        connected = True
        sock.close()
    except:
        connected = False
    return connected


if __name__ == '__main__':
    check_args()
    host = sys.argv[1]
    output_file = sys.argv[2]

    spreadsheet = csv.writer(open(output_file, 'w'), delimiter=',')
    spreadsheet.writerow(['Host', 'Port', 'Connected', 'Datetime'])

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        future_result = {executor.submit(tcp_connect, host, port): port for port in range(1, 65535+1)}
        for future in concurrent.futures.as_completed(future_result):
            port = future_result[future]
            try:
                did_connect = future.result()
                try:
                    spreadsheet.writerow([
                        host,
                        str(port),
                        str(did_connect),
                        str(datetime.now())])
                except Exception as e:
                    print('[-] Error writing to spreadsheet. %s' % e)
                if did_connect:
                    print("[+] %d connected" % port)
            except Exception as e:
                print('Error pulling result from future. %s' % e)