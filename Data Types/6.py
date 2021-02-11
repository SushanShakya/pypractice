# Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

import re

d = input("Enter a text: ")

x = d.split(" ")

pattern1 = "poor"
pattern2 = "not"

# poor = 0
# nott = 0

# counter = -1

poor = d.find(pattern1)
nott = d.find(pattern2)

# for i in x:
#     if(i.startswith(pattern1)):
#         poor = counter + 1
#     if(i.startswith(pattern2)):
#         nott = counter + 1
#     counter += len(i)

if poor > -1  and nott> -1 :
    # both are present
    start = poor if poor < nott else nott
    end = poor+4 if poor > nott else nott+3
    frontText = d[0:start]
    backText = d[end:]

    print(frontText + "good" + backText)
    
elif poor < 0 and nott < 0:
    # both not present
    print("poor and not both Not Found")
else:
    # One is present
    if(poor > -1):
        print("Found poor at index : {}".format(poor))
    else:
        print("Found not at index : {}".format(nott))
