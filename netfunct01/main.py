#!/usr/bin/env python3

# import
import json

# function
def devicereboot(devicedict):

    for ip in devicedict.keys():
        print(f"Connection to.. {ip}")
        print("REBOOTING NOW")


# function to push commands
def commandpush(devicecmd):  # devicecmd==dict

    for ip in devicecmd.keys():  # looping through the dict
        print(f'Handshaking. .. ... connecting with {ip}') # fstring
        # code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
            # code that sends cmds to device here
    return None


# start our main script
def main():
    """called at runtime"""

    # old dict, now using json file
    # devicecmd = {
    #     "10.1.0.1":["interface eth1/2", "no shutdown"],
    #     "10.2.0.1":["interface eth1/1", "shutdown"],
    #     "10.3.0.1":["interface eth1/5", "no shutdown"]
    # }

    with open("devicecmd.json", "r") as data_file:
        devicecmd = json.loads(data_file)

    print("Welcome to the network device command pusher")  # welcome message

    # get data set
    print("\nData set found\n")  # replace with function call that reads in data from file

    # run commandpush
    commandpush(devicecmd)  # call function to push commands to devices

    # run devicereboot
    devicereboot(devicecmd)


# call our main function
main()

