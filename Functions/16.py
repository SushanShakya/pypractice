# Write a Python program to square and cube every number in a given list of
# integers using Lambda.

sqr = lambda x: x**2
cub = lambda x: x**3

sample = [1,12,32,10]

sqred = list(map(sqr, sample))
cubed = list(map(cub, sample))

print(sqred)
print(cubed)