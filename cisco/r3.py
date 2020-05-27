#!/usr/bin/env python3

import getpass
import sys
import telnetlib


def connect_device(host, user, password):
    print(f'connecting to{host} with username {user} and password {password}')
    tn = telnetlib.Telnet(host)

    tn.read_until('Username: '.encode('latin-1'))
    tn.write(f"{user}\n".encode('latin-1'))
    tn.read_until('Password: '.encode('latin-1'))
    tn.write(f"{password}\n".encode('latin-1'))
    tn.read_until('Router# '.encode('latin-1'))
    tn.write('conf t'.encode('latin-1'))
    print(tn.read_all())
    '''
    tn.read_until('Router(config)# '.encode('latin-1'))
    tn.write('int fa0/1\nip addr 192.168.1.251 255.255.255.0\n'.encode('latin-1'))
    tn.write('no shut\n'.encode('latin-1'))
    tn.write('exit\n'.encode('latin-1'))
    '''


def main():
    host = sys.argv[1]
    user = sys.argv[2]
    #password = getpass.getpass()
    password = sys.argv[3]    
    #connect_device(host,user,password) 
    print(f'connecting {host}:{user}:{password}')
    
    tn = telnetlib.Telnet(host)
    
    tn.read_until('Username: '.encode('latin-1'))
    tn.write(f'{user}\n'.encode('latin-1'))
    tn.read_until('Password: '.encode('latin-1'))
    tn.write(f'{password}\n'.encode('latin-1'))
    tn.read_until('Router#'.encode('latin-1'))
    tn.write('conf t\n'.encode('latin-1'))
    tn.read_until('Router(config)#'.encode('latin-1'))
    tn.write('int fa 0/1\n'.encode('latin-1'))
    tn.read_until('Router(config-if)#'.encode('latin-1'))
    tn.write('ip addr 19.18.1.251 255.255.255.0'.encode('latin-1'))
    tn.read_until('Router(config-if)#'.encode('latin-1'))
    tn.write('no shut\n'.encode('latin-1'))
    tn.read_until('Router(config-if)#'.encode('latin-1'))
    tn.write('exit'.encode('latin-1'))
    tn.read_until('Router(config)#'.encode('latin-1'))
    tn.write('exit'.encode('latin-1'))
    
if __name__ == '__main__':
    main()


