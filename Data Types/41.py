# Write a Python program to convert a tuple to a string.

t = 1,2,3,4,

toStr = lambda x : str(x)

s = "".join(map(toStr, t))

print(s)