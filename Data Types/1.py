# Write a Python program to count the number of characters (character
# frequency) in a string. Sample String : google.com'

c = 'google.com';

freq = {}

for i in c :
    if(i in freq):
        freq[i] +=1
    else:
        freq[i] = 1
    
print(freq)