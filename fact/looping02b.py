#!/usr/bin/env python3
"""
For - looping across a file opened with 'with'
"""

def main():
    with open("dnsservers.txt", "r") as dnsfile:
        dnslist = dnsfile.readlines()

        for svr in dnslist:
            print(svr, end="")
    # no need to close the file
    # it's automatically closed when the 'with' statement ends    

main() 
