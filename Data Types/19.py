# Write a Python program to get the smallest number from a list
def smallest(l):
    smallest = l[0]
    for i in l:
        if(i < smallest):
            smallest = i
    
    return smallest

print(smallest([10,23,4]))
