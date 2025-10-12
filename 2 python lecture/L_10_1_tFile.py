# learnign t file 

'''
# x - creating a file
with open('L_10_1.txt', 'x') as f:
    f.write('This is f\n')
'''
    

# r - reading the content inside the file
with open('L_10_1.txt', 'rt') as f:
    print(f.read())

# w - changing the previous content by writing new ones
with open('L_10_1.txt', 'wt') as f:
    f.write('This is the second line\n')

# a - adding new lines into the current file without removing the previous ones
with open('L_10_1.txt', 'at') as f:
    f.write('This is the third line.\n')


with open('L_10_1.txt', 'rt') as f:
    print(f.read())





