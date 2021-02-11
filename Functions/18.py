# Write a Python program to check whether a given string is number or not
# using Lambda.

s = input("Enter a string : ")

isNumber = lambda x: x.isnumeric()

print(isNumber(s))