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


# my_car = vehicles['fiesta']
# print(my_car)
#
#
# computer = vehicles['virago']
# print(computer)
#
#
# learner = vehicles.get('ER5')
# print(learner)


vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "bombardier Learjet 75"
vehicles["toy"] = "glider"

vehicles["virago"] = "Yamaha"
# for key in vehicles:
#     print(key, vehicles.get(key), sep=",")

del vehicles["starfighter"]
#del vehicles["f1"]
result = vehicles.pop("f1", None)
print(result)
plane = vehicles.pop("learjet")
print(plane)
bike = vehicles.pop("tenere", "nnnnn")
print(bike)
for key, value in vehicles.items():
    print(key, value, sep=", ")
