# Write a Python script to check whether a given key already exists in a
# dictionary.

dict = {"a" : 1, "b" : 2}

key = input("Enter key : ")

if key in dict:
    print("Key found.")
else:
    print("Key not found.")