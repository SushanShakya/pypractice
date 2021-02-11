# Write a Python program to find if a given string starts with a given character
# using Lambda.

character = "x"

startsWith = lambda c: c.lower().startswith(character.lower())

d = input("Enter a string : ")

if(startsWith(d)):
    print("{} starts with {}".format(d, character))
else:
    print("{} doesn't start with {}".format(d, character))