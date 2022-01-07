#!/usr/bin/env python 3
"""
function grab bag challenges
"""


# return the maximum number of three inputs
def maxOfThree(num1, num2, num3) -> int:
    return max(num1, num2, num3)


# return the sum of a list
def listSum(nums: list):
    return sum(nums)


# return the product of a list
def listMult(nums: list) -> int:
    product = 1
    for num in nums:
        product *= num
    return product


# return true or false depending on if the parameter is in the given range
# range is -100:100
def isInRange(num: int) -> bool:
    samplerange = range(-100, 101)
    result = True if (num in samplerange) else False
    return result


# find the number of upper and lower case chars in a string
def calculateCase(words: str):
    upper = 0
    lower = 0

    for char in words:
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1

    return [upper, lower]


# check whether a string is a palindrome or not
def isPalindrome(words: str) -> bool:
    forward = words
    backwards = words[::-1]
    return True if (forward == backwards) else False


# sample data
sampleNumList1 = [2, 77, 109, 22, 543]
sampleString1 = "Do you know the Muffin Man?"
sampleString2 = "racecar"


# number functions
print("Number functions: ")
print("max of three numbers: ", maxOfThree(15, 600, 123))
print("sum up a list: ", listSum(sampleNumList1))
print("multiply all numbers in a list: ", listMult(sampleNumList1))
print("in range?: ", isInRange(-101))


# string functions
print("\nString functions: ")
caseResults = calculateCase(sampleString1)
print(f"# of uppercase characters: {caseResults[0]}\n"
      f"# of lowercase characters: {caseResults[1]}")
print("is first string a palindrome?: ", isPalindrome(sampleString1))
print("is second string a palindrome?: ", isPalindrome(sampleString2))

