#!/usr/bin/env python3
"""
using CSV lib to work with CSV data
"""

import csv


def main():
    with open("csv_users.txt", "r") as csvfile:
        # counter for unique file names
        i = 0

        for row in csv.reader(csvfile):
            i += 1
            filename = f"admin.rc{i}"

            # create and write a new file for data with 'open' & 'with'
            with open(filename, 'w') as rcfile:
                rcfile.write(f"export OS_AUTH_URL={row[0]}\n"
                             f"export OS_IDENTITY_API_VERSION=3\n"
                             f"export OS_PROJECT_NAME={row[1]}\n"
                             f"export OS_PROJECT_DOMAIN_NAME={row[2]}\n"
                             f"export OS_USERNAME={row[3]}\n"
                             f"export OS_USER_DOMAIN_NAME={row[4]}\n"
                             f"export OS_PASSWORD={row[5]}\n")

        print("admin.rc files created")


main()

