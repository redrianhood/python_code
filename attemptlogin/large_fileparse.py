#!/usr/bin/python3
"""
being careful about memory
"""


def main():
    # parse keystone.common.wsgi and return number of failed login attempts
    loginfail = 0  # counter for fails

    # open the file for reading
    keystone_file = open("/home/student/python_code/attemptlogin/keystone.common.wsgi", "r")
    
    for line in keystone_file:
        # if 'fail pattern' appears in line
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
            
    print("number of failed attempts is: ", loginfail)
    
    keystone_file.close()


main()

