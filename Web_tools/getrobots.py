#!/usr/bin/env python3 -tt
#-*- coding: utf-8 -*-
import re
import requests
encoding_str='latin-1'
'''
    This function retrieves each entry in the robots.txt file and returns a nested dictionary
'''
def get_disallow(sess,resp,regex_s,root_url):

    ary=[]
    hidden=re.findall(regex_s,resp.content.decode())

    for i in hidden:
        ary.append(i.encode(encoding_str).strip())
        
    cache={}
    
    for i in ary:
        url=""
        url=root_url+i.decode()
        resp=sess.get(url)
        cache.update({bytes(root_url+i.decode(),encoding_str):{i:resp.content}})

    return cache

'''
    This function processes the nested dictionaries and outputs the data to seperate files 
'''
def write_resp(cache):

    bytes_written=0
    try: 
        for key, val in cache.items():
            for k,v in val.items():
                k=(k.decode().replace('/',''))
                with open(k+'.resp', 'wb') as f:
                    bytes_written+=f.write(key)
                    bytes_written+=f.write(bytes('\n',encoding_str))
                    bytes_written+=f.write(v)
    except Exception as e:
        print('Error encountered: {}'.format(e))

    finally:
        return bytes_written
        
def main():
    '''
    Doctype: This script is used to scrape the disallowed directories in the robots.txt file under the root directory. 
    '''
    root_dir=r'http://192.168.1.161/security/2' # next iteration will allow for argument parsing of the root directory
    robots=r'/robots.txt' #still up in the air if I want to leave this or make it an arg

    regex_s=r'Disallow:\s(.+)' #re string that returns all Disallow directories

    # get the robots.txt data
    url=root_dir+robots
    sesh=requests.session() #start a session for scalability
    resp=sesh.get(url) #make the request

    cache = get_disallow(sesh,resp,regex_s,root_dir)
    bytes_written = write_resp(cache)
    print('Files written successfully, {} Bytes written!'.format(bytes_written))
    
if __name__ == '__main__':
    main()


'''
    Why is this even necessary?

    Read this excerpt from an SEO website concerning robots.txt:

    Also, if you happen to have sensitive data on your site that 
    you do not want the world to see, you will also prefer that 
    search engines do not index these pages (although in this 
    case the only sure way for not indexing sensitive data is to 
    keep it offline on a separate machine). 
    # http://www.webconfs.com/what-is-robots-txt-article-12.php
    
    The sure way is too keep it offline, but that is rarely the 
    case... 


'''