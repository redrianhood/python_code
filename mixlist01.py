#!/usr/bin/env python3

my_list = ["192.168.0.5", 5060, "UP"]

print("First item in list (IP): " + my_list[0])
print("Second item in list (port): " + str(my_list[1]))
print("Last item in list (state): " + my_list[2])

iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

print("IP address only: ", iplist[3], ", and", iplist[4])
