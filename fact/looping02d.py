#!/usr/bin/env python3
"""
For - looping across a file opened with 'with'
      while also being gentle on memory consumption.
      Sort domains ending in .ord and .com into files
      org-domain.txt and com-domain.txt
"""

def main():
    # open file in read mode
    with open("dnsservers.txt", "r") as dnsfile:    # 'r' is read mode
        # loop across lines in the file
        for svr in dnsfile:
            svr = svr.rstrip('\n')  # remove newline character if exists
            # IF the string svr ends with 'org'
            if svr.endswith('org'):
                with open("org-domain.txt", "a") as svrfile:    # 'a' is append mode
                    svrfile.write(svr + '\n')
            # ELSE-IF the string svr ends with 'com'
            elif svr.endswith('com'):
                with open("com-domain.txt", "a") as svrfile:  # 'a' is append mode
                    svrfile.write(svr + "\n")

    # no need to close

main() 
