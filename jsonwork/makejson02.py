#!/usr/bin/python3
"""
The json.dumps() function creates a JSON string
"""

import json


def main():
    """runtime code"""
    # data blob to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
                   {"name": "Arthur Dent", "species": "Human"}]

    # display python data
    print(hitchhikers)

    # create JSON string
    jsonstring = json.dumps(hitchhikers)
    print(jsonstring)


if __name__ == "__main__":
    main()
