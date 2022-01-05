#!/usr/bin/env python3
"""
Alta3 Study
"""

def main():

    # creating a small string
    lilstring = "Currently taking a Python coding class from Alta3"
    # split on " "
    newlist = lilstring.split(" ")
    # print newlist
    print(newlist)

    # create list of strings
    myiplist = ["10", "0", "0", "4"] 
    # join with "."
    singleip = ".".join(myiplist)
    # display new list
    print(singleip)

main()
