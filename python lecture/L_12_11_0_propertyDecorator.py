# property decorator
# we use this '@property' decorator on any method in the class to use the method as a peoperty


class Student:
    def __init__(self, phy, chem, math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"     # here we created an instance attribute 'self.percentage'

    def calculate_percentage(self):
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    # you can do the above by using the property decorator
    @property
    def give_percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


s1 = Student(98,97,99)
print(s1.percentage)
print('*******************************************************************')

s1.phy = 86
print(s1.phy)              # changing the value of one subject
print(s1.percentage)       # after changing the value of phy the percentage should change, but it didn't changed
print('*******************************************************************')

s1.calculate_percentage()
print(s1.percentage)       # new percentage will be printed
print('*******************************************************************')

print(s1.give_percentage)   # you dont need to put paranthese "()" while using property operator


