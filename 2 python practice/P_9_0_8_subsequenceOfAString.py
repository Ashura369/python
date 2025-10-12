# printing subsequence of a string

s = "abc"

def sub(s, idx=0, curr=""):
    if idx == len(s):
        print(curr)   # print one subsequence
        return
    
    # Choice 1: include current character
    sub(s, idx+1, curr + s[idx])
    
    # Choice 2: exclude current character
    sub(s, idx+1, curr)


sub(s)
