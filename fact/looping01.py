#!/usr/bin/env python3
"""
For - a simple for loop
"""

def main():
    # for-loop is perfect for stepping through this list
    iplist = ["10.1.1.1", "10.2.2.2", "10.3.3.3"] # list of IP (str)

    # 'ip' is just a variable as we step through iplist
    for ip in iplist:
        print(ip)

main()
