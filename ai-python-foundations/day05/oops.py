'''OOPS
bank application
acc number
cutomer name
balance

deposit
withdraw
check balance

class
    object
    abs
    enc
    inh
    poly

    '''
'''Car - class - blueprint

my_car
friend_car
brother_car'''
class Car:
    pass
class Car1:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.make} {self.model} engine has started.")

    def stop_engine(self):
        print(f"The {self.make} {self.model} engine has stopped.")
my_car=Car1("Toyota", "Camry", 2020)
my_car.start_engine()
my_car.stop_engine()
