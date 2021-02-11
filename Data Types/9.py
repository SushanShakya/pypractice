# Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.

def exchange(e):
    data = list(e)
    tmp = data[0]
    data[0] = data[-1]
    data[-1] = tmp
    return "".join(data)

inp = input("Enter a string : ")

inp = exchange(inp)

print(inp)