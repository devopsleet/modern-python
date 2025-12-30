thinkers = ['Plato', 'PlayDo', 'Gummy']

while True:
    try:
        thinker = thinkers.pop()
        print(thinker)

    except IndexError as e:
        print("We tried to pop up too many thinkers")
        print(e)
        break


class FancyCar():
    wheels = 4

    def drivefast(self):
        print("Driving fast")

myCar = FancyCar()
print(myCar.wheels)
myCar.drivefast()
