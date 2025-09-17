# learning inheritance
# when one class (child / derived) derives the properties and methods of another class (parent / base) 

class Car:
    @staticmethod
    def start():
        print('CAR STARTED')

    @staticmethod
    def stop():
        print('CAR STOPPED')


class ToyotaCar (Car):
    def __init__(self, name):
        self.name = name




