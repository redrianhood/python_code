#!/usr/bin/env python3
"""
Conditionals - testing if strings test true
"""

def main():

    ipchk = input("Input an IP address: ")

    # a string tests as True
    if ipchk == "192.168.70.1":
        print(f"IP address of Gateway set to {ipchk}, this is not recommended.")
    elif ipchk:
        print("Looks like the IP address was set to: " + ipchk)
    else:
        print("No input provided")

main()
