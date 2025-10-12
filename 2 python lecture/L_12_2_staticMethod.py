# learning static method
# these methods dont use the 'self' as parameter (work at class level)


class Student:
    @staticmethod       # called 'decorators'   # if you make  3 non-parameterized methods (methods with no self), then you have to  make 3 '@staticmethod' for each methods
    def hello():        # in static methods you can neither use any attribute nor any function from the parent class
        print('WELCOME TO THE WORLD')
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def word(self):  # this makes print(s1) meaningful
        return f"Name of the person is {self.name}, and his marks are {self.marks}"


# *******************************************************************************************



s1 = Student('ABC', [99, 84, 97])
s2 = Student('DEF', [99, 84, 97])

s1.hello()

print(s1.word())
print(s2.word())








