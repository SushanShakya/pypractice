# Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


x = input("Enter a string : ")

def isUpper(x):
    if(ord(x) >= 65 and ord(x) <=90):
        return True
    else:
        return False

def isLower(x):
    if(ord(x) >=97 and ord(x) <= 122):
        return True
    else:
        return False

def count(s):
    value = {
        "uppercase" : 0,
        "lowercase" : 0,
        "others" : 0
    }
    for i in s:
        if(isUpper(i)):
            value["uppercase"] += 1
        elif(isLower(i)):
            value["lowercase"] += 1
        else:
            value["others"] += 1
    return value


values = count(x)

print("No. of Upper case characters : {}".format(values['uppercase']))
print("No. of Lower case characters : {}".format(values['lowercase']))
