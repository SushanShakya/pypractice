# Write a Python program to remove the characters which have odd index
# values of a given string.

def rmOdd(s):
    d = list(s)
    for i in range(len(d)):
        if(i %2 !=0):
            d[i] = ''

    return "".join(d)

x = input("Enter a string : ")

x = rmOdd(x)

print(x)