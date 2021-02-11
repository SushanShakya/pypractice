# Write a Python program to remove an item from a tuple.

t = 1,2,3,

l = list(t)

l.remove(1)

t = tuple(l)

print(t)