# using private on variable

"""

In Python, private variables and methods are mainly used to enforce encapsulation, which helps in protecting sensitive data and hiding unnecessary implementation details. For example, in a bank account class, the account balance should not be directly accessible or modifiable from outside, because someone could easily set it to an invalid value. By making the balance variable private, we ensure that any change happens only through controlled methods like deposit() or withdraw(), where proper validation can be applied. Similarly, private variables are useful for maintaining consistency in data, such as ensuring that a person’s age is always positive by restricting direct access and using setter methods for validation. Private methods, on the other hand, are often internal helper functions that simplify complex operations but are not intended to be called directly by users, which keeps the class interface clean and reduces the risk of misuse. Overall, the practical use of private members is to protect data integrity, prevent errors, and provide a safer, more reliable design.

"""


class Student:
    def  __init__(self, name, password):
        self.name = name
        self.__password =  password       # if you put two underscore before password in 'self.password', then the  password becomes private

    def show_password(self):
        return self.__password


s1 = Student("Ravi", 25)

print(s1.name)
# print(s1.password)       # if you run this wil throw error

# as private variables cant be printed through print statement, so to print then you have to make a method and then you can access the password

print(s1.show_password())

print('**********************************************************************')
# using private on methods
class Person:
    __name = 'Ashura'

    def __intro(self, name):
        print(name)

    def access(self):
        self.__intro(self.__name)




p1 = Person()

# p1.__intro()        # will throw error
p1.access()           # you can access a private method through another method







