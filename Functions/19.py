# Write a Python program to create Fibonacci series upto n using Lambda.

from functools import reduce

getNew  = lambda x, _: x+[x[-1]+x[-2]]
 
fibonacci = lambda n: reduce(getNew,range(n-2), [0, 1])

x = input("Enter value of n : ")

print(fibonacci(int(x)))