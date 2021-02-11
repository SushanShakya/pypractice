# Write a Python program to multiplies all the items in a list.

def multiply(x):
    prod = 1
    for i in x:
        prod *= i
    return prod

print(multiply([5,3]))
