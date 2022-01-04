#!/usr/bin/env python3
"""
Alta3 Study
List - simple list
"""

def main():
    # list creation
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list
    print(list1)

    print(list1[1])   # arista_eos

    # new list with single item
    list2 = ["juniper"]

    # extend list1 by list2 (comibe both into a single list)
    list1.extend(list2)

    # list1 now contains 'juniper'
    print(list1)

    # create another list
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    # append operation
    list1.append(list3)

    # display new, complex list
    print(list1)

    print(list1[4])     # list of IP addresses 
    print(list1[4][0])  # first IP listed

    animals = ["dog", "cat", "fox", "cow", "bee"]
    print(animals)

main()
