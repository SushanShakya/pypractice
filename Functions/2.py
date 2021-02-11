# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20


def sumAll(l):
    sum = 0
    for i in l:
        sum += i
    return sum

print(sumAll([1,2,3,4,5]))