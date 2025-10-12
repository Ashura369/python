# for loop
for i in range(1, 6):
    print(i)

'''
range() is a built-in function in Python that generates a sequence of numbers.
It doesn't create a list directly, but an iterator (like a lazy sequence) that produces numbers when you loop over it.
'''

print("**********************************************")

# while loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1      # you cant use "count ++" like java or python
