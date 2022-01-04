#!/usr/bin/env python3

## a dictionary
dictionary = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}
 

## display parts of the dictionary
print( dictionary["hostname"] )
print( dictionary["ip"] )

## requested a 'fake' key
#print( dictionary["lynx"] )  

## request a 'fake' key with .get()
print("1st test - .get()")
print( dictionary.get("lynx") )

print("2nd test - .get()") 
print( dictionary.get("lynx", "The key is in another castle!"))

print("3rd test - .get()")
print( dictionary.get("version"))

print("4th test - .keys()")
print( dictionary.keys())

print("5th test - .values()")
print( dictionary.values())

print("6th test - .pop()")
dictionary.pop("version")
print( dictionary.keys())
print( dictionary.values())

print("7th test - ADD a new value")
dictionary["adminlogin"] = "karl08"
print( dictionary.keys())
print( dictionary.values())

print("8th test - ADD a new value")
dictionary["password"] = "qwerty"
print( dictionary.keys())
print( dictionary.values())
