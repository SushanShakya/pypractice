# Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself

inp = input("Enter a string : ")


def replaceChars(d):
    if len(d) == 0:
        return ""
    req = d[0]
    data = list(d)
    for i in range(len(data)):
        if i == 0:
            continue
        else:
            if data[i].lower() == req.lower():
                data[i] = "$"
    
    return "".join(data)

inp = replaceChars(inp)
print(inp)
