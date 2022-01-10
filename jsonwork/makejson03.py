#!/usr/bin/python3
"""
opening a static file containing JSON data
"""

import json


def main():
    """runtime code"""
    # open file
    with open("datacenter.json", "r") as datacenter:
        datacenter_string = datacenter.read()

    # display the decoded string
    print(datacenter_string)
    print(type(datacenter_string))
    print("\nThe code above is string data. Python cannot easily work with this data.")
    input("Press Enter to continue\n")

    # create JSON string
    datacenter_decoded = json.loads(datacenter_string)

    # This is now a dictionary
    print(type(datacenter_decoded))

    # display servers in datacenter
    print(f"1 servers: {datacenter_decoded}")

    # display the servers in row3
    print(f"2 row3: {datacenter_decoded['row3']}")

    # display the 2nd server in row2
    print(f"3 2nd server, row2: {datacenter_decoded['row2'][1]}")

    # display last server in row3
    print(f"4 last server in row3: {datacenter_decoded['row3'][-1]}")


if __name__ == "__main__":
    main()

