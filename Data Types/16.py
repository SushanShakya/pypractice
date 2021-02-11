# Write a Python program to sum all the items in a list.

def sumAll(l):
    sum = 0
    for i in l:
        sum += i
    return sum

print(sumAll([1,2,3,4,5]))
