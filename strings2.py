
parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])

print(parrot[-1])
print(parrot[-14])

print(parrot[0:6])
print(parrot[3:5])
print(parrot[:9])
print(parrot[10:])
print(parrot[:])
print(parrot[:6] + parrot[6:])


letters = "abscdefghijklmnopqrstuvwxyz"

# Slice with Negative numbers
print(parrot[-4:-2])
print(parrot[-4:12])

print(parrot[0:6:2])
print(parrot[0:6:3])
number = "9,227,343,56565656"
separators = number[1:4]
print(number[1::4])


values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

# negative step
