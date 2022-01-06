#!/usr/bin/env python3
"""
exploring network interfaces
"""

# import statements
import netifaces


def return_ip():
    name = netifaces.i


def main():
    print(netifaces.interfaces())

    for interface in netifaces.interfaces():
        # interface title
        print(f"\n**************Details of Interface - {interface} *********************")
        # details of the interface (and iterations on the value we're getting)
        # print(netifaces.ifaddresses(interface))
        # print(netifaces.ifaddresses(interface)[netifaces.AF_LINK])

        print("looking at: ", netifaces.ifaddresses(interface))

        try:
            print("MAC address: ", netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr'])
            print("IP address: ", netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr'])
        except:
            print('Could not collect adapter information')


main()


