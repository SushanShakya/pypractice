# Write a Python program to sort a list of tuples using Lambda.

x = [(1,2), (0, 10), (-1, 1)]

sortL = lambda x: list(sorted(x))

print(sortL(x))