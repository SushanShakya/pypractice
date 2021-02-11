# Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).

# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

x = input("Enter comma separated words : ")

l = x.split(",")

l.sort()

filtered = []

for i in l :
    if(i not in filtered):
        filtered.append(i)

print(filtered)
