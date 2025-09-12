# removing the duplicates from a list

list = [1,2,3,0,1,2,3,3,2,4,4,65,45,6,33,1,1,22,2,2,4,1,8,656,6,8,8,9]


def remove(list, idx=0, newList = None):
    if newList is None:
        newList = []

    list = sorted(list)     # sorting the list

    if idx is len(list): # idx == len(list)
        return newList

    if list[idx] not in newList:
        newList.append(list[idx])
    
    
    return remove(list, idx+1, newList)


print(remove(list))