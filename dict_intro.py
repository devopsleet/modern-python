vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple'
}

vehicles["starfighter"] = "lockhead F-104"
vehicles["learjet"] = "bombardier"
vehicles["toy"] = "glider"
# my_car = vehicles['fiesta']
# print(my_car)
#
# commuter = vehicles['virago']
# print(commuter)
#
# learner = vehicles.get("er5")
# print(learner)


# for key in vehicles:
#     print(key, vehicles[key], sep= ";")


# Upgrade the virago
vehicles["virago"] = "Yamaha 350"

del vehicles["starfighter"]
# del vehicles["f1"]
result = vehicles.pop("f1", "The key does not exist")
plane = vehicles.pop('learjet')
print(plane)
print(result)
for key, value in vehicles.items():
    print(key, value, sep=", ")
