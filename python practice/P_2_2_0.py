# taking input of a specific type

num = int(input("Enter a number: "))

# Check the type
if type(num) == str:
    print("This is a string")
else:
    print("This is an integer:", num)