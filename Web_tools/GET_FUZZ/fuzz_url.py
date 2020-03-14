#!/usr/bin/env python3
import json
import requests
import sys


class FUZZ:
    def __init__(self, headers=None, proxies=None, verify=None,
                 url=None):
        self.headers = headers
        self.proxies = proxies
        self.verify = verify
        self.url = url
        self.sesh = requests.session()


def burp_proxies():
    return {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}


def get_json(fname):
    with open(fname) as json_file:
        return json.load(json_file)


def get_wordlist(fname):
    with open(fname, 'r') as f:
        return f.readlines()


def blind_fuzz(fuzz, wordlist):
    for i in wordlist:
        #print(fuzz.headers['host'])
        try:
            resp = fuzz.sesh.get(fuzz.url+i.rstrip(), verify=fuzz.verify,
                                 proxies=fuzz.proxies, headers=fuzz.headers)
            print(resp.status_code)
            if resp.status_code == 404 or resp.status_code == 400:
                continue
            elif resp.status_code == 403:
                with open('responses_403', 'a+b') as f:
                    f.write(('\n' + fuzz.url+i).encode('latin-1'))
                    f.write('\n'.encode('latin-1'))
                    f.write(resp.content + '\n'.encode('latin-1'))
            else:
                with open('responses', 'a+b') as f:
                    f.write(('\n' + fuzz.url+i).encode('latin-1'))
                    f.write('\n'.encode('latin-1'))
                    f.write(resp.content + '\n'.encode('latin-1'))
        except Exception as e:
            print(f'Exception encountered:{e}!')
            continue


def main(args):
    url = args[0]
    headers = get_json(args[1])
    headers['host'] = '' 
    wordlist = get_wordlist(args[2])
    if len(args) < 4:
        proxies = burp_proxies()
    else:
        proxies = get_json(args[3])
    fuzz = FUZZ(url=url, headers=headers, proxies=proxies, verify=False)
    blind_fuzz(fuzz, wordlist)


if __name__ == '__main__':
    main(sys.argv[1:])
