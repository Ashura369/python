# print all the letters in a string

def str(a, idx=0):
    if idx == len(a):
        return
    
    ans = a[idx]
    print(f'{a[idx]}', end="")
    str(a, idx+1)

str('Biswajeet Pradhan')



