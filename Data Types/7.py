# Write a Python function that takes a list of words and returns the length of the
# longest one

def longest(words):
    if(len(words) <1):
        return 0
    longest = len(words[0])
    for word in words:
        currentLen = len(word)
        if(currentLen > longest):
            longest = currentLen
    return longest

sample = ["abc", "sheer", "sherifsa"]

print(longest(sample))