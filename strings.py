parrot = "Norwegian Blue"

print(parrot[0:6]) # Norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[9:])
print(parrot[10:])


print(parrot[:6])


print(parrot[:6] + parrot[6:])
print(parrot[:])


letters = "abcdefghijklmnopqrst"


print(parrot[-4:-2])

print(parrot[-4:12])


print(parrot[-14:-8])

print(parrot[0:6:2])
print(parrot[0:6:3])


number = "9,223;323:098 456;807"
separators = number[1::4]
values = "".join(char if char not in separators else " " for char in number).split()
print(values)
print([int(val) for val in values])
