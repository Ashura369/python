import array

arr1 = array.array('i', [1,2,3,4,5])                # i = integer
arr2 = array.array('f', [1.65,2.97,58.58,8.46])     # f = float

# there is no such way you can enter string into a array in python

print(arr1)
print(arr2)
print('-'*120)
# *******************************************************************************************


# index
print(arr1[0])
print(arr1[-1])     # prints last element

print('-'*120)
# *******************************************************************************************


# append
arr1.append(6)  # adds element to the last index
print(arr1)

print('-'*120)
# *******************************************************************************************


# insert element at specific index
arr1.insert(0, 0)   # (index, element)
print(arr1)

print('-'*120)
# *******************************************************************************************


# remove element (by value)
arr1.remove(6)
print(arr1)

print('-'*120)
# *******************************************************************************************


# pop
arr1.pop()  # automatically removes the last element
print(arr1)

arr1.pop(4) # removes the element at 4th index
print(arr1)

print('-'*120)
# *******************************************************************************************


# index of an element
print(arr1.index(2))    # prints index of an element

print('-'*120)
# *******************************************************************************************


# count - occurance of an element
arr1.append(3)
arr1.append(3)
arr1.append(3)

print(arr1.count(3))
print(arr1)

print('-'*120)
# *******************************************************************************************


# converting to list
a = arr1.tolist()
print(a)
print(type(a))

print('-'*120)
# *******************************************************************************************


arr1.reverse()  # reversing the entire array
print(arr1)

print('-'*120)
# *******************************************************************************************


# sorting an array
arr1 = array.array('i', sorted(arr1))
print(arr1)
    # you can also use for loop (refer chat gpt)

print('-'*120)
# *******************************************************************************************


# removing the duplicates
    # well there is no such way to remove the duplicates in an array
    # hence to do so, you have to use set

arr1 = set(arr1)    # arr1 = array.array('i', sorted(set(arr1))) [you can also do this so that you can sort the array and also remove the duplicates at the same time]
print(arr1)

print('-'*120)
# *******************************************************************************************


# converting a set back into an array
arr1 = array.array('i', arr1)
print(arr1)









