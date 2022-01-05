#!/usr/bin/env python3

def main():
    """
    Basic script to test out python conditionals
    """

    # collect input from user
    hostname = input("What value should we set for hostname? ")

    # test if input matched expected value using .lower()
    if hostname.lower() == "mtg":
        print("hostname found to be mtg")
        print("hostname matches expected config")
    else:
        print("provided hostname does not match config")

    # always display to user
    print("exiting the script")
main()
