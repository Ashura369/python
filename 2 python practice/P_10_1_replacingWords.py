# replaceing word java with python

file = r'D:\THE CODE\python\python practice\P_10_1.txt'

print('*'*120)
with open(file, 'w+') as f:
    f.write('I am a new commer, i like java so much. \nHence i decided to choose a fullstack java career in it')
    f.seek(0)
    data = f.read()
    print(data)

print('*'*120)
print(data)     # you can print the data declared inside the file
print('*'*120)
changes = data.replace('java', 'python')
print(changes)  # remember you have stored the changed value in one obj, so to changed the data in the file, you need to overwrite it


with open(file, 'w+') as f:
    f.write(changes)
    print(f.read())



