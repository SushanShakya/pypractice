# Write a Python program to remove the nth
# index character from a nonempty
# string.

def remove(s, n):
    d = list(s)
    d[n] = ''
    return "".join(d);

s = "salsa"

s = remove(s, 1)
print(s)

