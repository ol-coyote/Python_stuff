#!/usr/bin/python3
#badchars_generator.py
import string
tmp = []
with open('badchars.txt','w') as f:
	for i in string.hexdigits[:16]:
		for j in string.hexdigits[:16]:
			f.write("%" + i + j +'\n')