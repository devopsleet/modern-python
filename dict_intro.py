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
vehicles["starfighter"] = "Locked F-104"
vehicles["learjet"] = ["bombardier lier jet"]
vehicles["toy"] = "glider"

#
# del vehicles["sdcsdsds"]



output = vehicles.pop('er51', 'This key does not exist')
print(output)

nums = [1,2,3,4,5]
print(nums.pop(2))
#
# for key, value in vehicles.items():
#     print(key, value, sep= ", ")


# Upgarde the virag
