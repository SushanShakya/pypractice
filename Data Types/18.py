# Write a Python program to get the largest number from a list.

def largest(l):
    largest = l[0]
    for i in l:
        if(i > largest):
            largest = i
    
    return largest

print(largest([10,23,4]))
