# Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def getEvens(l):
    evens = []
    for i in l:
        if(i%2==0):
            evens.append(i)

    return evens

sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Sample List : {}".format(sample) )
print("EvenList : {}".format(getEvens(sample)) )