#!/usr/bin/env python3
"""
study on 'for' logic
"""

def main():
    # a list to iterate through
    vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
    # loop across the list
    for vendor in vendors:
        print("the vendor is: " + vendor)
    print("\nThe loop has ended")

main()
