"""
encapsulation -- wrapping data and functions into a single unit (object)

"""

class Student:
    def __init__(self, name, marks):
        self.name = name          # public
        self._marks = marks       # protected (convention: use with care)
        self.__grade = None       # private (name mangling)

    def show(self):
        print(f"Name: {self.name}, Marks: {self._marks}, Grade: {self.__grade}")

    # proper use of abstraction
    def set_grade(self, grade):
        if grade in ["A", "B", "C", "D", "F"]:
            self.__grade = grade
        else:
            print("Invalid grade")

    def get_grade(self):
        return self.__grade

# ----------------------------------------------------------------------

# Usage
s1 = Student("ABC", 92)

print(s1.name)        
print(s1._marks)    

s1.set_grade("A")
print(s1.get_grade())  

s1.show()













