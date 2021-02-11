# Write a Python program to sum all the items in a dictionary.

d = {0: 10, 1: 20}

s = 0

for key in d:
    s += d[key]

print(s)
