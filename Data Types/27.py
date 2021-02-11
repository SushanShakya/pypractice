# Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

l1 = [1, 3, 5, 7, 9, 10]
l2 = [2, 4, 6, 8]

reqList = l1[0: len(l1) - 1] + l2

print(reqList)