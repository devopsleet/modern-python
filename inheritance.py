class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    pass

c = Car()
c.start()
