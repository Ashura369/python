# removing duplicates


a = [1, 2, 2, 3, 4, 4, 5]

# to do so you have to use set 
print(list(set(a)))  # approach 1
print(set(a))        # approach 2

'''******************************************************************************'''
# using set
# you can do the same by, converting it into a set
b = set(a)
print(b)