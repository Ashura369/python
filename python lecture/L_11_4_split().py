# learning split

line = 'python is fun'
words = line.split(' ')     # removes the white  spaces in the line   # REMEMBER WHEN YOU USE SPLIT, AFTER USING IT THE VALUE GETS STORED IN A LIST, HENCE THE VALUES ARE STROED IN 'words' AS A LIST
print(words)

print('************************************************************')

# turning string into a number

line2 = ['1,2,3,4,5,6,7,8,9,10']      # SPLIT ONLY WORKS ON STRINGS, NOT LISTS
line3 = '1,2,3,4,5,6,7,8,9,10'

# nums = line2.split(',')             # will throw error
numsAsString = line3.split(',')
numsAsInt    = [int(x) for x in numsAsString]

        
'''
BELOW IS THE SIMPLIED CODE OF numsAsInt

numsAsInt = []
for x in line3.split(','):
    numsAsInt.append(int(x))
'''

numsAsInt2 = []                 # declaring the obj as a list
for x in numsAsString:          # as the values are returned as list after split they are being stored in x
    numsAsInt2.append(int(x))   # afterwords each value of x is converted into an integer

print(numsAsString)
print(numsAsInt)
print(numsAsInt2)

print('************************************************************')


# split by characters 
name = 'BISWAJEET PRADHAN'
a = name.split()
b = list(name)
print(a)
print(b)

name = name.split(' ')
name = list(name)
print(list(name))

'''at the end i tried to split the space and then again i tried to split all the letters in the name. But remember when you try to use split on a list which is already a list, it will not work it will simply create a copy of itself. And further more you cant use split on list, can only use on strings but still you were using it on a already splitted list'''

print('************************************************************')

name2 = 'jeet'
print(list(name2))











