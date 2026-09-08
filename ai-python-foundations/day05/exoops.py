class Car:
    def start(self):
        print("Car engine started")
class BMW(Car):
    def start(self):
        print("BMW engine started")
class Tesla(Car):
    def start(self):
        print("Tesla engine started")
class Audi(Car):
    def start(self):
        print("Audi engine started")
bmw=BMW()
tesla=Tesla()
audi=Audi()
bmw.start()
tesla.start()
audi.start()