# Write a Python program to insert a given string at the beginning of all items in
# a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']


sample = [1,2,3,4]
st = "emp"

addStr = lambda x: "".join([st, str(x)])


sample = list(map(addStr,sample))

print(sample)
