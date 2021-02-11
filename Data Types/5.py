# Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.

# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'


def addSuffix(c):
    if(len(c) < 3):
        return c
    
    lastThree = c[-3:]

    if(lastThree == "ing"):
        return c + "ly"
    else:
        return c + "ing"

inp = input("Enter a string : ")

inp = addSuffix(inp)
print(inp)
