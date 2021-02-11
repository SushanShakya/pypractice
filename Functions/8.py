# Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def distinct(l):
    req = []
    for i in l:
        if(i not in req):
            req.append(i)
    return req

sample = [1,2,3,3,3,3,4,5]

print("Unique List : {}".format(distinct(sample)))