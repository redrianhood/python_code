#!/usr/bin/env python3
"""
exploring read
"""

## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
print("configfile.read() result: ", configfile.read())

## close file
configfile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
print("result of .readlines(): ", configlist)

## Iterate through configlist
print("iterating through readlines list:")
for x in configlist:
    # print(x)
    # prints as:
        # vlan 5
        #
        #   name VOICE
        #
        # vlan 10
        #
        #   name DATA

    # print(x, end="")
    # prints as:
        # vlan 25
        #   name DEV
        # vlan 30
        #   name DB

    # print(x.strip())
    # prints as:
        # vlan 25
        # name DEV
        # vlan 30
        # name DB

    print(x.splitlines())
    # prints as:
        # ['vlan 5']
        # ['  name VOICE']
        # ['vlan 10']
        # ['  name DATA']

## Always close your file
configfile.close()

