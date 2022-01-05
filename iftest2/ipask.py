#!/usr/bin/env python3
"""
Conditionals - testing if strings test true
"""

def main():

    ipchk = input("Input an IP address: ")

    # a string tests as True
    if ipchk:
        print("Looks like the IP address was set to: " + ipchk)
    else:
        print("No input provided")

main()
