class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self,engine):
        self.engine = Engine()

    def start(self):
        self.engine.start()


class ElectricEngine:
    def start(self):
        print("Electric motor start")

c = Car(ElectricEngine())
c.start()
