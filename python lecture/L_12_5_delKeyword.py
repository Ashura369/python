# del keyword

class Student:
    def  __init__(self, name):
        self.name = name

s1 = Student("Ravi")

print(s1.name)

# del - deleting
del s1.name         # you can also delete an entire object ie 's1'
print(s1.name)      # will throw error





