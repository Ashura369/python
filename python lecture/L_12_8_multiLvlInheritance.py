# MULTI LVL INHERITANCE

# learning inheritance
# when one class (child / derived) derives the properties and methods of another class (parent / base) 


"""
in py if you do multi lvl inheritance from one class which again inherits some values from another class so my current class will inherit attributes from both the classes

    Class C inherits from class B

    Class B inherits from class A

    Then class C gets attributes/methods from both B and A


"""


class Car:
    color = 'Black'

    @staticmethod
    def start():
        print('CAR STARTED')

    @staticmethod
    def stop():
        print('CAR STOPPED')


class ToyotaCar (Car):

    def __init__(self, brand):
        self.brand = brand
    
    def run(self):
        print('THE CAR IS RUNNING')


class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

c1 = Fortuner("PETROL")
c1.start()
c1.run()