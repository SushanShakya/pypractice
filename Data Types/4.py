# Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.

def swapCharacters(a,b, swap_length):
    if(len(a) < swap_length or len(b) < swap_length):
        print("++ ERROR ++")
        return ""
    else:
        s1 = list(a)
        s2 = list(b)

        for i in range(swap_length):
            tmp = s1[i]
            s1[i] = s2[i]
            s2[i] = tmp
        
        s1 = "".join(s1)
        s2 = "".join(s2)

        return s1 + " " + s2

sample = ["abc","xyz"]

print(swapCharacters(sample[0], sample[1], 2))
    


    
    