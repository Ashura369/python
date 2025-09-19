# learning class method
# a class method is bound to the class and receives the class as an implicit first argument
# static method cant access or modify class state and generally for utility

class Person:
    name = 'Raghu'

    def changeName(self, name):
        self.name = name
    
    # type 1
    def changeName2(self, a):       # assigning values into the name attribute of the 'Person' class, using "person.name"
        Person.name = a
    
    # type 2
    def changeName3(self, a):       # assigning values into the name attribute of the 'Person' class, using "self.__class__.name"
        self.__class__.name = a

    # type 3
    @classmethod                    # decorator
    def changeName4(cls, a):        # assigning values into the name attribute of the 'Person' class, using "@classmethod"
        cls.name = a


p1 = Person()
p1.changeName('Ranjan')
print(p1.name)          # Ranjan
print(Person.name)      # Raghu

print('**********************************************************************')

p1.changeName2('Kishan')
print(p1.name)
print(Person.name)

print('**********************************************************************')

p1.changeName3('Georgy')
print(Person.name)

print('**********************************************************************')

p1.changeName4('Sophia')
print(Person.name)







