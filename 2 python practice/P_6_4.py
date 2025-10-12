list = ['A', 'B', 'C', 'D', 'E', 'F']
i = 0

while True:
    newList = list[i % len(list)]   

    dict = {
    'letters' : newList

    }

    print(dict)

    i+=1

""" 
How it behaves:
When i = 0 → 0 % 6 = 0 → letters[0] = 'A'
When i = 1 → 1 % 6 = 1 → letters[1] = 'B'
When i = 2 → 2 % 6 = 2 → letters[2] = 'C'
When i = 3 → 3 % 6 = 3 → letters[3] = 'D'
When i = 4 → 4 % 6 = 4 → letters[4] = 'E'
When i = 5 → 5 % 6 = 5 → letters[5] = 'F'


👉 Now the trick happens:
When i = 6 → 6 % 6 = 0 → back to letters[0] = 'A'
When i = 7 → 7 % 6 = 1 → back to letters[1] = 'B'

"""



