# learning + type file
# this allows for the read + write together in a file, hence there is no need to write separate codes to do both the task

fileName = r'D:\THE CODE\python\python lecture\L_10_3.txt'

'''
with open(fileName, "x+") as f:
    f.write("This is a new file created using x+.")
    f.seek(0)  # move cursor back to start  # if you comment out this line py will try to read from the current position, But since the pointer is already at the end of file, nothing is left to read → it prints empty.
    print(f.read())
'''

# w
with open(fileName, 'w+') as f:
    f.write('Hii my name is Biswa')
    f.seek(0)
    print(f.read())


# r
print('************************************************')
with open(fileName, 'r+') as f:
    print(f.read())

    f.seek(0)
    print(f.read())
print('************************************************')

# a 
with open(fileName, 'a+') as f:
    f.write('My age is 25.\n')
    f.write('I love coding.')
    f.seek(0)
    print(f.read())



