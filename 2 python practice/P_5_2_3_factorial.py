# finding factorial


# using for loop
a = [1,2,3,4,5]

b = 1
for i in a:
    b *= i

print(b)


print('*' * 120)
# ***********************************************************************

# using while loop
n = 1
i = 0
while i < len(a):
    n *= a[i]
    i+=1

print(n)

print('*' * 120)
# ***********************************************************************

# using math.factorial
import math     # to do it,  you have to import 'math'
print(len(a))   # 5
print(math.factorial(len(a)))
print(math.factorial(5))


print('*' * 120)
# ***********************************************************************

# using math.prod
print(math.prod(a))










