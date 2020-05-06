#!/bin/python3
import requests
import sys
import time


# Method for defining proxies, initial run is through localhost proxy,
# can be modified for a remote proxy.
def get_proxies(): 
    return {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
    }


# Define headers for requests, bypassing the python user agent string
# since some servers will not respond correctly without a valid UA.
def get_headers():
    return {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate'
    }
    
# This method should be modified to reflect the payload data
# sent to the server. For a generic template this has been setup with 
# the most basic payload.
def get_payload(user,passwd):
        return {
        'username':  user, 
        'password':  passwd
    }
    
    
def main(): 
	# Setup proxy and headers
    proxies=get_proxies()
    headers=get_headers()
	
    # configure host and creds for testing
	# URI is the main login page
    URI = "" #sys.argv[1]
	# URI2 is the page for posting the login information
	URI2 = '' #sys.argv[2]
    username = "" #sys.argv[3]
    password = "" #sys.argv[4]
	
	# grab 1000 cookies for analysis
	for i in range 1000:
		try: 
			sesh = requests.session()
			resp = sesh.get(URI, verify=False, proxies=proxies,headers=headers)
			payload = get_payload(username,password)
			resp = sesh.post(URI2, verify=False, proxies=proxies, headers=headers, data=payload, cookies=resp.cookies)
			print(f"response code: {resp.status_code}\nresponse headers: {resp.headers}\nresponse cookies: {resp.cookies}")
			with open(f"{time.time()}_resp_cookies.html",'w') as f:
				f.write(resp.cookies.decode('latin-1'))
		except Exception as e:
			print(f"Exception encountered: {e}")
    
if __name__ == "__main__":
    main()