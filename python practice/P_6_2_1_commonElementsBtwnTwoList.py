# finding the common elements btwn two lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

a = set(list1)
b = set(list2)

common = a & b
print(common)

