# dictionary are used to store data values in key:value pairs
# unordered, mutable(changable) & do not allow duplicate keys


dictionaries = {
    'name' : 'Biswajeet',
    'age' : 25,
    'language' : 'python',
    'is adult ???' : True,
    1 : [1,2,3,4,5] # storing the list into a integer
}

print(dictionaries)
print('*********************************************')
print(type(dictionaries))
print('*********************************************')
print(dictionaries["name"])
print('*********************************************')
print(dictionaries[1])
print('*********************************************')

# changing the values
dictionaries['name'] = 'BISWAJEET'
print(dictionaries)
print('*********************************************')

# making a new key
dictionaries['surname'] = 'PRADHAN'
print(dictionaries)
print('*********************************************')

# how to add surname after name
dictionaries['name'] = dictionaries['name'] + ' ' + dictionaries['surname'] 
print(dictionaries)
print('*********************************************')





