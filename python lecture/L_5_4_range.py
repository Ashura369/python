# using range to make list

nums = list(range(1, 51))
print(nums)
print('****************************************************************************')
numsEven = list(range(0, 51, 2))
print(numsEven)
print('****************************************************************************')
numsOdd = list(range(1, 51, 2))
print(numsOdd)
print('****************************************************************************')
reverse = list(range(51, 1, -2))
print(reverse)
print('****************************************************************************')

# list comprehension
numsMultiply = [2**i for i in range(1, 11)]
print(numsMultiply)







