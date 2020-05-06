#!/usr/bin/python3
#badchars_generator.py
import string

# This method is called to generate character encoding payloads in various HTML
# encoding schemes. These payloads can then be used in a fuzzing application to 
# test for encoding.
def generate_encoded_files():
	tmp = []
	# output will be formated as : "%NN" where N is the character in the string
	with open('badchars1.txt','w') as f:
		for i in string.hexdigits[:16]:
			for j in string.hexdigits[:16]:
				f.write(f"%{i}{j}\n")
				
    # output will be formated as : "&#NN" where N is the character in the string
	with open('badchars2.txt','w') as f:
		for i in string.hexdigits[:16]:
			for j in string.hexdigits[:16]:
				f.write(f"&#x{i}{j}\n")	

    # output will be formated as : "&#xNN" where N is the character in the string
	with open('badchars3.txt','w') as f:
		for i in range(0xffffff + 0x1):
			f.write(f"&#{i:06}\n")

    # output will be formated as : "#xNNNNNN" where N is the character in the string
	with open('badchars4.txt','w') as f:
		for i in range(0xffffff + 0x1):
			tmp = hex(i)[2:]
			l_tmp = len(tmp)
			if l_tmp % 6:
				tmp = ("0" * (6-l_tmp)) + tmp
			f.write(f"&#x{tmp}\n")


def main():
	try:
		generate_encoded_files()
	except Exception as e:
		print(f"Execption encountered trying to generate encoded payloads: \n{e}\n")


if __name__ == '__main__':
	main()
		