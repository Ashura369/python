# deleting a file
# to do so you have to import 'import os'

import os
file = r'D:\THE CODE\python\python lecture\L_10_4.txt'

with open(file, 'w+') as f:
    f.write('This is the file')
    f.seek(0)
    print(f.read())

# os.remove(file)   # first run the code and then uncomment this line and then run the code, you wil see that the code is deleted 
