# finding max and min element of an array

import array
arr = array.array('i', [15, 7, 22, 3, 19])


print(max(arr))
print(min(arr))

print('-'*120)
# ***********************************************************************************

# using for loop
max = arr[0]
min = arr[0]
for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i

print(max)
print(min)

print('-'*120)
# ***********************************************************************************


# using while loop


max2 = arr[0]
min2 = arr[0]

i = 0
while i < len(arr):
    if arr[i] > max2:
        max2 = arr[i]
    if arr[i] < min2:
        min2 = arr[i]
    i += 1

print(max2)
print(min2)

