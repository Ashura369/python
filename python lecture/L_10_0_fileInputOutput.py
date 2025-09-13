# to perform operations on a file (read & write data)
'''
types
    text files      - .txt, .docx, .log, etc (file that stores data in character form like text or symbols)
    binary files    - .mp4, .mov, .png, .jpeg, etc (file that stores data in any form other than the character form)

    To open a file we have to do below;
        f = open("file_name", "mode") # mode = type read or type write   

        data = f.read()

        f.close()

        
    r  ->	Read mode (default). Opens file for reading. Error if file doesn’t exist.
    w  ->	Write mode. Creates a new file or overwrites an existing one.
    x  ->	Exclusive creation. Creates a new file but throws an error if it already exists.
    a  ->	Append mode. Opens file for writing, adds content at the end without deleting existing data.
    b  ->	Binary mode. Used for files like images, videos, etc. (rb, wb).
    t  ->	Text mode (default). Used for text files (rt, wt).
    +  ->	Update mode. Allows reading + writing together (r+, w+, a+).
'''

# opening a file
book = open("D:\THE CODE\python\python lecture\L_10_1.txt", "r")    
# 'r' stands for the read mode

# reading a file
print('*'*120)
data = book.read()
print(data)
print(type(data))

book.close()

# rather than writing a code that you have to close at the end of the code, you can do the below
print('*'*120)

with open(r"D:\THE CODE\python\python lecture\L_10_1.txt", "r") as book:
    data = book.read()
    print(data)
    print(type(data))

# **********************************************************************
print('*'*120)

# Exclusive Create (x)
with open(r"D:\THE CODE\python\python lecture\L_10_2.txt", "x") as book2:
    book2.write("A new text file created using 'x ")        # REMEMBER if a text file on this name 'L_10_2.txt' already exists just delete that and then run this code or else it will throw error

# Read file with 'r'
with open(r"D:\THE CODE\python\python lecture\L_10_2.txt", "r") as book2:
    data = book2.read()
    print(data)

# Overwrite file with 'w'
with open(r"D:\THE CODE\python\python lecture\L_10_2.txt", "w") as book2:
    book2.write("This is file x")
   
# Read again to confirm overwrite
with open(r"D:\THE CODE\python\python lecture\L_10_2.txt", "r") as book2:
    data = book2.read()
    print(data)

# **********************************************************************
print('*'*120)

# append - adding new content into the file with out deleting the previously stored data

with open(r"D:\THE CODE\python\python lecture\L_10_2.txt", "a") as book2:
    book2.write('\n And now i have made some changes and have added new texts into it, without deleting the previous details')

with open("D:\THE CODE\python\python lecture\L_10_2.txt", "r") as book2:
    data = book2.read()
    print(data) 

# **********************************************************************
print('*'*120)





