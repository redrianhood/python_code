#!/usr/bin/env python3
"""
For - using a files' lines as a source for the for-loop
"""

def main():
    # open file in read mode
    dnsfile = open("dnsservers.txt", "r")
    # creating list of lines
    dnslist = dnsfile.readlines()

    # 'ip' is just a variable as we step through iplist
    for svr in dnslist:
        print(svr, end="")
    
    dnsfile.close()

main()
