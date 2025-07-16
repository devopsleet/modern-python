class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kenwood = Kettle("kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75

hamilton = Kettle("Hamilton", 14.55)

print("Models = {} {} {} {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Kettle Objets")
print("Kenwood pricing")


print("Models : {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))
print("Models : {0.make}")
print(f"Objet " {object.create})
print("Object is in use")
print()
