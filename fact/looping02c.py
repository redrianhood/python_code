#!/usr/bin/env python3
"""
For - looping across a file opened with 'with'
      while also being gentle on memory consumption
"""

def main():
    with open("dnsservers.txt", "r") as dnsfile:
        for svr in dnsfile:
            print(svr, end="")

main() 
