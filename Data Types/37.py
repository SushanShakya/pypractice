# Write a Python program to multiply all the items in a dictionary.

d = {0: 10, 1: 20}

s = 1

for key in d:
    s *= d[key]

print(s)
