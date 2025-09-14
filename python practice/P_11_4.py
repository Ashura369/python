# converting a string into a list and counting how many words and characteres are there


line = 'I love Python Programming.'
toList = list(line)        # converts string into characters
toWord = line.split()      # splits into words

# type 1 (manual counting)
countChars = 0
countWords = 0

# loop through characters
for i in toList:
    print(i, end=", ")
    countChars += 1

print()

# loop through words
for j in toWord:
    print(j, end=", ")
    countWords += 1


print()
print("\nTotal characters (manual):", countChars)
print("\nTotal words (manual):", countWords)

print('*******************************************')

# type 2
print('total characters:', len(toList))


print('*******************************************')

# type 3
line = line.split()

print(line)
print('total words: ', len(line))




















