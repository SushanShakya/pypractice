# Write a Python program to count the occurrences of each word in a given
# sentence.

x = input("Enter a sentence : ")

occur = {}

words = x.split(" ")

for word in words:
    if(word in occur):
        occur[word] += 1
    else:
        occur[word] = 1

print(occur)