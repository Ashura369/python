# learning tuples
# a built-in data type that lets us create immutable sequences of values

n1 = (1,2,3,4,5,6,7,8,9,10)
# unlike list it cant be changed, we cant use append, add, remove, etc

print(n1)
print(type(n1))

n2=(1)
print(n2)       # will be printed as a int, to avoid doing so you have to put comma after it
n3 = (1,)
print(n3)       # will be printed as a tuple
print(type(n2)) # int
print(type(n3)) # tuple

# finding the first occurance of an element in the list
print('it first occured at idx ',n1.index(5))

# counting the total occurances of an element
print('total no. of occurance of element 3 in the list is ', n1.count(3))