# Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.

def unknown(x):
    given = input("Enter the unknown number : ")

    return x * int(given)

print(unknown(10))