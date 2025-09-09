# making lists

nums = [1,2,3,4,5,6,7,8,9,10]   # it may look similar to array, but its not array
print(nums)
print(type(nums))   
print(nums[0])

for i in nums:
    print('the number is: ', i)


# printing the number with idx 
for idx, value in enumerate(nums):
    print('the number at index', idx, 'is', value)

# in java strings are immutable, they cant be changed
a = 'hii'
a = 'name'
print(a[0])
# a[0] = 'y'     # if you uncomment this it will throw error

print(a[0])
    