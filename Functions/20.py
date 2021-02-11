# Write a Python program to find intersection of two given arrays using
# Lambda

arr1 = [1,2,3,4,5,6]
arr2 = [3,4,5,7]

intersection = lambda x: x in arr2

req = list(filter(intersection, arr1))

print(req)