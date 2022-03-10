##################################
# VIOLENT PYTHON CODE - REFERENCE#
##################################
import optparse
from socket import *
import sys


def connScannGrabbing(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        result = connSkt.connect_ex((tgtHost, tgtPort))
        if result ==0:
            print (f'[+] {getservbyport(tgtPort)} => {tgtPort}/tcp open')
            raijin_bytes = str.encode("Raijin\r\n")
            connSkt.sendall(raijin_bytes)
            results = connSkt.recv(1024)
            print(f'[+] RESULT: {results.decode("utf-8", "ignore")}\n')
        #connSkt.connect((tgtHost, tgtPort))
        connSkt.close()
    except KeyboardInterrupt:
        print("\n[-] You pressed Ctrl+C\n")
        sys.exit()
    except gaierror:
        print('[-] Hostname could not be resolved. Exiting\n')
        sys.exit()
    except error:
        print ("[-] Couldn't connect to server\n")
        #sys.exit()


def portScan(tgtHost, tgtPorts):
    tgtIP = tgtHost
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(f'[-]Cannot resolve {tgtHost} unknown host')
    try:
        tgtName = gethostbyaddr(tgtIP)
        print(f'\n[+]Scan results for: {tgtName[0]}')
    except:
        print(f'\n[+]Scan results for: {tgtIP}')
    setdefaulttimeout(1)
    print(f'[+]Scanning ports from {int(tgtPorts[0])} to {int(tgtPorts[1])}\n')
    for tgtPort in range(int(tgtPorts[0]),int(tgtPorts[1])+1):
        connScannGrabbing(tgtHost, int(tgtPort))


def main():
    parser = optparse.OptionParser(
        'usage %prop -H'+'<target host> -p <target port>')

    parser.add_option('-H', dest='tgtHost', type='string',
                      help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string',
                      help='specify target range port by using ":" ')

    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = options.tgtPort.split(':')
    if (tgtHost == None) | (tgtPorts == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)


if __name__ == "__main__":
    main()
