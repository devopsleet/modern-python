class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)


hamilton = Kettle("Hamilton", 18)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
