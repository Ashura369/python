# print a string in reverse

def rev(a, idx = None):
    if idx == None:
        idx = len(a)-1
    
    if idx < 0:
        return 
    
    print(a[idx], end="")
    rev(a, idx-1)


a = input('enter something to get the reverse: ')

rev(a)
