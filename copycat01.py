#!/usr/bin/env python3
"""
Pushing files around using shutil and os from the standard library
"""
# IMPORTS
import shutil
import os

def main():
    # forces Python program to 'start' in home user directory
    # ie. move into the working directory
    os.chdir("/home/student/python_code")

    # shutil.copy will copy a single file at the given path to the folder at the given destination 
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # shutil.copytree will copy an entire folder w/ subfolders
        # making a new folder if one does not exist
    os.system("rm -rf /home/student/python_code/5g_research_backup/") ##INV
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":  ##INV
    main()
