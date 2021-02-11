# Write a Python program to remove duplicates from a list

def removeDuplicate(l):
    filtered = []

    for i in l:
        if(i not in filtered):
            filtered.append(i)

    return filtered

print(removeDuplicate([1,2,1,1]))