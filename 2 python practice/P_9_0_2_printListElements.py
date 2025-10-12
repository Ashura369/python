# print all elements in a list

def r1(list, idx=0):
    if idx == len(list):
        return
    
    print(list[idx], end=" ")
    r1(list, idx+1)

# ************************************************************************

'''another method for doing the same'''
def r2(lst):
    if not lst:          # base case: if list is empty, stop
        return
    
    print(lst[0], end=" ")   # print first element
    r1(lst[1:])     


list = ["a","b","c","d","e","f","g","h","i","j"]
r1(list)

print()

r2(list)
