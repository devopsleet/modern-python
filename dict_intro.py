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
# commuter = vehicles['virago']
# print(commuter)
#
#
# learner = vehicles.get("eR5")
# print(learner)

vehicles["starfighter"] = "Lockehead F-104"
vehicles["learjet"] = "bombardier Learjet"
vehicles["toy"] = "glider"


vehicles["virago"] = "Yamaha XV535"
# for key in vehicles:
#     print(key, vehicles[key], sep = ", ")


#del vehicles["starfighter"]
result = vehicles.pop("f1", "Good!!!!")
print(result)

plane = vehicles.pop("learjet")
print(plane)
for key, value in vehicles.items():
    print(key, value, sep = ", ")
