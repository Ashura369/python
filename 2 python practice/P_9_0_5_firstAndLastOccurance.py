# print first and last occurrence of a letter in a given string

def firstOccr(s, find, idx=0):
    if idx == len(s):
        print(f"'{find}' not found in {s}")
        return
    
    if s[idx] == find:
        print(f"The letter '{find}' occurs first at index {idx} in the string '{s}'")
        return

    firstOccr(s, find, idx+1)


def lastOccr(s, find, idx=None):
    if idx is None:
        idx = len(s)-1

    if idx < 0:
        print(f"'{find}' not found in {s}")
        return

    if s[idx] == find:
        print(f'The last occurance of letter {find} is at index {idx} in letter {s}')
        return
    
    lastOccr(s, find, idx-1)


firstOccr("Biswajeet Pradhan", "a")
lastOccr("Biswajeet Pradhan", "a")
