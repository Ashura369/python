nums = [1,2,3,4,5,6,7,8,9,10]

print('from idx 1 to idx 6',nums[1:6]) # will not print the 6th idx element

print(nums[-4:-1])  # -1 = 10

print('**************************************')

# sorting
n1 =[1,9,8,65,87,5,2,26,4,45,6]
print(n1.sort()) # right it will sort the list but it will print none, so print n1 again and the list will be sorted
print(n1)

# append -- will add element to the very last idx
n1.append(999)
print(n1)

# printing the list in reverse order
n1.sort(reverse = True)
print(n1)

# insert
n1.insert(1, 888) # inserting 888 at idx 1
print(n1)

# remove
n1.remove(87)   # removing element 87
print(n1)

# pop - removes element at idx
n1.pop(0)
print(n1) # removes element at idx 0