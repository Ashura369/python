a = 'jeet'
b = 'pradhan'

# concatination
print(a+b)
print()

# len - printing the length of the string
print(len(a))
print(len(b))
print()

# indexing
print(a[0]) # printing the 0 th element of 'a'

# slicing
print(a[0:4]) # printing element from 0 to the 4th element (although 4th element doesnt exist it doesn't matter)
# if you remove the 4th element and keep it as a[0:] / a[0: len(a)] it will print til the last element
# a[: 4] from first to the last  element

# backward slicing
print(a[-4:-1]) 

# endswith
print(a.endswith("et")) # wheather its ends with et or not

# capitalize
print(a.capitalize())  # Output: 'Jeet'

# replace
print(a.replace('jeet', 'biswajeet'))  # Output: 'biswajeet'

# find -  returns the first occurance of the substring
# returns -1 find found nothing
a = 'jeet pradhan'
print(a.find('pradhan'))  # Output: 5
print(a.find('xyz'))      # Output: -1

# count - returns how many times a string is getting repeated
a = 'jeet pradhan jeet'
print(a.count('jeet'))  # Output: 2
print(a.count('a'))     # Output: 2

