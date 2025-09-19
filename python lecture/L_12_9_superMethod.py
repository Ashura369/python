# learning super method
# this method is used to access methods of the parent class

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print('CAR STARTED')

    @staticmethod
    def stop():
        print('CAR STOPPED')


class ToyotaCar (Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)     # here we have assigned parameter 'type' which has been passed into the 'type' parameter in the __init__ which is inside the Car class

        # you can also write "self.type = type" but that would have assigned values into the "type" parameter of __init__ function which is inside the ToyotaCar function

        self.start()    # it will look for the start() methoed inside the current class, if it present, then will run that. If there is no start method in the current class, it will directly go t0 the parent class will look for the start method and execute that

        super().start() # it will automatically go to the parent class and run the start method over there 


c1 = ToyotaCar("PRIUS", "ELECTRIC")
print(c1.type)











