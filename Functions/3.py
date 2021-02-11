# Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def mulAll(l):
    prod = 1
    for i in l:
        prod *= i
    return prod

print(mulAll([1,23,4]))