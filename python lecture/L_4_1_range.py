# range functions returns a sequence of numbers, starting from 0 by default, and increments by 1(by default), and stops before a specified number

seq = range(10)
print(seq[1]) # print 1st index
print(seq[2])

print('-'*120)
# ************************************************************

# using loop over range
print('The range is -- ', end=' ')
for i in range(10):     # end
    print(i, end=' ')

print()
# ************************************************************

for i in range(2, 10): # (start, end)
    print(i, end=" ")

print()
# ************************************************************

for i in range(3, 20, 2):   # (start, end, by how much the number will increase)
    print(i, end=" ")
print()
# ************************************************************


# HENCE PRINTING EVEN AND ODD NUMS BECOMES EASY USING RANGE
# YOU CAN ALSO PRINT NUMBERS IN REVERSE ORDER

for i in range(100, 1, -5): # for decreasing order you have to write the number as negative integer
    print(i, end=" ")

print()

# can also take input to do so
# make sure that while taking input you must receive them as an int, by default they are received as string
a = int(input('enter start number - '))
b = int(input('enter end number - '))
c = int(input('enter the multiplication number - '))

for i in range(a, b):
    print(i * c, end=", ")

