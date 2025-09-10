# printing the sum of all the arr elements

import array
arr = array.array('i', [10, 20, 30, 40, 50])

print(sum(arr))

print('-'*120)
# ***********************************************************************************

# printing using for loop
a = 0
for i in arr:
    a += i

print('for loop - ',a)
    
print('-'*120)
# ***********************************************************************************

# printing using while loop
i = 0
b = 0
while i < len(arr):
    b += arr[i]
    i+=1

print('while loop - ',b)














