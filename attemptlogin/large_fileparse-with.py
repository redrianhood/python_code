#!/usr/bin/python3
"""
being careful about memory
"""


def main():
    # parse keystone.common.wsgi and return number of failed login attempts
    loginfail = 0  # counter for fails

    # open the file for reading
    with open("/home/student/python_code/attemptlogin/keystone.common.wsgi") as kfile:

        # loop over the file
        for line in kfile:
            # if this 'fail pattern' appears in the line...
            if "- - - - -] Authorization failed" in line:
                loginfail += 1

    print("number of failed attempts is: ", loginfail)


main()

