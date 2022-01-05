#!/usr/bin/env python3
"""
simple script to take input and calculate hurricane severity  
"""

def severity():
    # prompt for unit of measurement for windspeed 
    unit = input("Is the wind in mph or km? ")
    unit_l = unit.lower()

    # unit validation
    # prompt for windspeed value 
    if unit_l == "mph":
        response = input("What is the wind speed in mph? ")
    elif unit_l == "km":
        response = input("What is the wind speed in km/h? ")
    else:
        print("Invalid unit of measurement for wind speed")
        return

    # change response to int and catch error if unable
    try:
        speed = int(response)
    except (ValueError):
        print("Invalid input, please input integer")
        return

    ## Return category if windspeed is in mph
    if unit_l == "mph":
        if speed >= 157:
            print("Category 5")
        elif speed >= 130:
            print("Category 4")
        elif speed >= 111:
            print("Category 3")
        elif speed >= 96:
            print("Category 2")
        elif speed >= 74:
            print("Category 1")
        else:
            print("Too slow to be classified as a hurricane")
    ## Return catagory if windspeed is in km
    elif unit_l == "km":
        if speed >= 252:
            print("Category 5")
        elif speed >= 209:
            print("Category 4")
        elif speed >= 178:
            print("Category 3")
        elif speed >= 154:
            print("Category 2")
        elif speed >= 119:
            print("Category 1")
        else:
            print("Too slow to be classified as a hurricane")

severity()
