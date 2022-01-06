#!/usr/bin/env python3
"""
nesting an if-statment inside of a for-loop
"""

def main():
    # a list to iterate through
    vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
    approved_vendors = ["cisco", "juniper", "big_ip"]

    # loop across the list
    for vendor in vendors:
        print("\nThe vendor is: " + vendor, end="")
        if vendor not in approved_vendors:
            print(" - NOT AN APPROVED VENDOR!", end="")

    print("\nThe loop has ended")

main()
