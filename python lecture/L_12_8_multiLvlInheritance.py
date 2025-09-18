# MULTI LVL INHERITANCE

# learning inheritance
# when one class (child / derived) derives the properties and methods of another class (parent / base) 


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


class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

c1 = Fortuner("PETROL")
c1.start()











