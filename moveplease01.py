#!/usr/bin/env python3
"""
A simple script to move two files into ceph_storage/ 
"""

# Standard Library Imports
import shutil
import os

def main():
    # 'start' in home directory
    os.chdir('/home/student/python_code/')

    # take care with .move, as it's easy to overwrite files
    # move raynor.obj in to ceph_storage dir
    shutil.move('raynor.obj', 'ceph_storage/')

    # prompt for new name and rename w/ .move
    xname = input('What is the new name for the kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
