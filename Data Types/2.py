# Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the
# empty string.

d = input("Enter a string : ")

if(len(d) < 2):
    print("Empty String")
else:
    print("{}{}{}{}".format(d[0],d[1],d[-2],d[-1]))