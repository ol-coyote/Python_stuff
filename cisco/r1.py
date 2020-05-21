#!/bin/python3
import getpass
import sys
import telnetlib

def conn_device(HOST):
    tn = telnetlib.Telnet(HOST)
    tn.read_until("Username: ".encode('latin-1'))
    tn.write("user\n".encode('latin-1'))
    tn.read_until("Password: ".encode('latin-1'))
    tn.write("password\n".encode('latin-1'))
    tn.write("enable\n".encode('latin-1'))
    tn.write('password\n'.encode('latin-1'))
    tn.write("conf t\n".encode('latin-1'))
    tn.write("int f 0/0\n".encode('latin-1'))
    tn.write("duplex full\n".encode('latin-1'))
    tn.write("no shut\n".encode('latin-1'))
    #tn.write("int loop 0\n".encode('latin-1'))
    #tn.write("ip addr 1.2.3.4 255.255.255.255\n".encode('latin-1'))
    #tn.write('no shut\n'.encode('latin-1'))
    tn.write("end\n".encode('latin-1'))
    tn.write("exit\n".encode('latin-1'))
    print(tn.read_all())
    
def main():
    HOST = sys.argv[1]
    print(f"Connecting to {HOST} via telnet!")
    conn_device(HOST)
    pass


if __name__ == '__main__':
    main()

