# learning inheritance
# when one class (child / derived) derives the properties and methods of another class (parent / base) 

"""
3 types of inheritance

single lvl inheritance
multi lvl inheritance
multiple inheritance


"""

# SINGLE LVL INHERITANCE

class Car:
    color = 'Black'

    @staticmethod
    def start():
        print('CAR STARTED')

    @staticmethod
    def stop():
        print('CAR STOPPED')


class ToyotaCar (Car):
    # here ToyotaCar will inherit all the methods and properties of Car

    def __init__(self, name):
        self.name = name


c1 = ToyotaCar('A')
c2 = ToyotaCar('B')

c1.start()      # since i have inherited all the properties of Car, i can use the methods inside the 'Car'
c1.stop()
print(c1.color)


