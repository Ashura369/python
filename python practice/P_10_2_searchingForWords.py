# make a function and searching for a word 'python' 
# make a funciton and print at which the word comes first

word = "python"

with open(r'D:\THE CODE\python\python practice\P_10_1.txt', 'r') as f:
    data = f.read()

    if data.lower().find(word) != -1:       #here we lower cased everthing
        print(f'word "{word}" found')
    else:
        print(f'word "{word}" not found')


'''making a function and doing the above again'''
print('*'*90)

def searchWord(word):
    with open(r'D:\THE CODE\python\python practice\P_10_1.txt', 'r') as f:
        data = f.read()

        # if the word is present in the file, the find keyword will return the index number of that word, if the word is not opresent it willr return -1

        if data.lower().find(word) != -1:       # here we lower cased everthing      # if (word in data)
            print(f'word "{word}" found')
        else:
            print(f'word "{word}" not found')


searchWord("java")
searchWord("python")

'''***********************************************************************'''
print('*'*90)

# printing the line number of the first occurance of the given word
def findLine(word):
    lineNo = 1

    with open(r'D:\THE CODE\python\python practice\P_10_1.txt', 'r') as f:
        for line in f:
            if (word.lower() in line):   # case-insensitive check
                print(f'word "{word}" first found at line {lineNo}')
                return lineNo
            lineNo += 1

    print(f'word "{word}" not found in file')
    return -1


# Test
findLine('python')
findLine('java')



