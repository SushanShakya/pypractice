# Write a Python program to filter a list of integers using Lambda.

getNumbers = lambda x: isinstance(x,int)

sample = ["this", 1, 21, "that", 10]

res = list(filter(getNumbers, sample))

print(res)
