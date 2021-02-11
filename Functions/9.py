# Write a Python function that takes a number as a parameter and check the
# number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that
# has no positive divisors other than 1 and itself.

def isPrime(x):
    if(x == 1):
        return None
        
    if(x %2 == 0 or x % 3 == 0):
        return False
    
    return True

x = input("Enter the number : ")

value = isPrime(int(x))

if(value is None):
    print("Unknown !")
elif(value):
    print("Prime.")
else:
    print("Not Prime")

