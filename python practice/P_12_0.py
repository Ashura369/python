class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def word(self):  # this makes print(s1) meaningful
        return f"Name: {self.name}, Marks: {self.marks}"


# Create object with arguments
s1 = Student('ABC', [99, 84, 97])
s2 = Student('DEF', [99, 84, 97])

# Print object
print(s1.word())
print(s2.word())

s1.name = 'IRON MAN'
print(s1.word())
