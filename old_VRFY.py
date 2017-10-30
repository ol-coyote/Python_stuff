#!/usr/bin/python
import socket
import sys
import errno

def main():
    if len(sys.argv) != 4:
        print "Usage: VRFY.py <username> <ip> <port>"
        sys.exit(0)

    with open(sys.argv[1]) as file:
            users = file.readlines()

    names =[]

    for i in users:
        names.append(i[:-1])

    users =[]

    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Connecting to: " + sys.argv[2] + " on port: " + sys.argv[3]
    try: 
        connect=s.connect((sys.argv[2],int(sys.argv[3])))
        banner=s.recv(2048)
        print banner
        for i in names: 
            s.send('VRFY ' + i + '\r\n')
            result = s.recv(1024)
            print result
        s.close()
    except socket.error as e:
        if e.errno == errno.ECONNREFUSED:
            print "Connection refused: " + str(e.errno) + " scanning next IP.\n"
            sys.exit(0)
        elif e.errno == errno.ETIMEDOUT:
            print "Connection timed out: " + str(e.errno) + " scanning next IP.\n"
            sys.exit(0)
        elif e.errno == errno.EHOSTDOWN:
            print "Host is down: " + str(e.errno) + " scanning next IP.\n"
            sys.exit(0)
        elif e.errno == errno.EHOSTUNREACH:
            print "No route to host: " + str(e.errno) + " scanning next IP.\n"
            sys.exit(0)
        else:
            raise

if __name__ == '__main__':
    main()

