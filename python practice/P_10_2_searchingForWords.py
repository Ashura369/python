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

        if data.lower().find(word) != -1:       #here we lower cased everthing      # if word in data
            print(f'word "{word}" found')
        else:
            print(f'word "{word}" not found')


searchWord("java")
searchWord("python")

'''***********************************************************************'''

def findLine(word):
    with open(r'D:\THE CODE\python\python practice\P_10_1.txt', 'r') as f:
        data = f.read()

        if (data.lower().search('word'))



