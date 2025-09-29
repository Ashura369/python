


'''NESTED DICTIONARIES'''
student = {
    'name': 'Biswajeet',
    'subjects': {
        'math': 10,
        'eng': 20,
        'hindi': 25
    },
    'age': 25,
    'language': 'python',
}

# Print entire student dictionary
print(student)
print('*********************************************')

# Accessing nested dictionary
print(student['subjects'])  # printing subjects which is inside student
print('*********************************************')

# Accessing a value inside the nested dictionary
print(student['subjects']['math'])  # printing math which is inside subjects
print('*********************************************')

# Using dictionary methods on main dictionary
print("Keys of student dictionary:", student.keys())
print("*********************************************")
print("Values of student dictionary:", student.values())
print("*********************************************")
print("Items of student dictionary:", student.items())
print("*********************************************")

# Using get() method - returns value of keys
print("Student's language using get():", student.get('language'))
print("Student's grade using get():", student.get('grade', 'THE VALUE NOT AVAILABLE'))  # if the key 'grade' is not available, then the "THE VALUE IS NOT AVAILABLE" will be printed
print("Student's grade using get():", student.get('grade'))  # key doesn't exist
print("*********************************************")


# Updating the main dictionary
student.update({
    'age': 26,                 # Updating age
    'grade': 'A'               # Adding a new key
})


print("After update:", student)
print("*********************************************")

# Using dictionary methods on nested 'subjects' dictionary
print("Subjects keys:", student['subjects'].keys())
print("Subjects values:", student['subjects'].values())
print("Subjects items:", student['subjects'].items())
print("*********************************************")

# Using get() in nested dictionary
print("Marks in Hindi using get():", student['subjects'].get('hindi'))
print("*********************************************")

# Updating nested dictionary
student['subjects'].update({'math': 15})  # changing math marks from 10 to 15
print("Updated subjects after changing math mark:", student['subjects'])

# printg the keys and values as list
print(list(student.keys()))
print(list(student.values()))
print("*********************************************")

# length
print('length of student : ',len(student))
print('length of keys : ',len(student.keys()))
print('length of values : ',len(student.values()))
print("*********************************************")

