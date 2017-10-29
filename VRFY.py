#!/usr/bin/python
import errno
import os.path as PTH
import pprint
import socket
import sys
import optparse as OP

# Function for parsing user args.
# First arg should specify the file containing user names.
# Second arg should specify the file containing the IP addresses to scan.
# Usage will specify the commands necessary to correctly execute the program.
# Function will test for correct number of arguments, and will exit if they are not provided. 
def get_args():
    parser = OP.OptionParser('usage%prog -U <username_file> -I <ip_file>')
    parser.add_option('-U', dest='tgtUser', type='string', help='specify file for user names')
    parser.add_option('-I', dest='tgtIP', type='string', help='specify file for IP Addresses')
    (options, args) = parser.parse_args()
    #print options
    tgtUser = options.tgtUser
    tgtIP = options.tgtIP
    if (tgtUser == None) | (tgtIP == None):
        print parser.usage
        sys.exit(0)
    return tgtUser,tgtIP

# Function used to check if the file exists within the system.
# @param filename requires valid filename and path in string.
# @return returns boolean to determine if the file exists. 
def check_file_exists(filename):
    return PTH.isfile(filename)

# function for retrieving file contents into a list
# @parma filename contains valid filename and path in string.
# @return contains contents of file if file exists, or exits gracefully if not. 
def get_file_contents(filename):
    contents=""
    if (check_file_exists(filename)):
        with open(filename, 'r') as file:
        contents = file.readlines()
        return contents
    else:
        print "File: "  + filename + " does not exist or does not have read permissions...exiting!"

# Function that creates a socket for connecting to SMTP port 25.
# @param ip contains IPv4 address in string format.
# @param users conatins list of known user names to test connection for.
# @return return 0 if successful, return -1 if error
def scan_host(ip,users):
    ip = ip[:-1]
    print "IP: "+ ip + " User: "+ users
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connect=s.connect((ip,25))
    except socket.error as e:
        if e.errno == errno.ECONNREFUSED:
            print "Connection refused: " + str(e.errno) + " scanning next IP.\n"
            return -1
        elif e.errno == errno.ETIMEDOUT:
            print "Connection timed out: " + str(e.errno) + " scanning next IP.\n"
            return -1
        elif e.errno == errno.EHOSTDOWN:
            print "Host is down: " + str(e.errno) + " scanning next IP.\n"
            return -1
        elif e.errno == errno.EHOSTUNREACH:
            print "No route to host: " + str(e.errno) + " scanning next IP.\n"
            return -1
        else:
            raise
    banner=s.recv(1024)
    print banner
    s.send('VRFY ' + users + '\r\n')
    result=s.recv(1024)
    print result
    s.close()
    return 0

#main function call
def main():
    userF, ipF = get_args()
    contents = get_file_contents(ipF)
    #users = 'root', 'user', 'test', 'tester', 'bob', 'alice'
    for i in contents:
        scan_host(i, 'root')

if __name__ == '__main__':
    main()
