parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])

# negative indexing
print()

print(parrot[13 -14])

print(parrot[0:6]) # Norweg

print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:14])
print(parrot[10:])
print(parrot[:])


print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])
print(parrot[:])

letters = "abcdefghijklmno"

print(parrot[-4:2])
print(parrot[-4:12])


print(parrot[0:6:2])


number = "9,223;372:036 854;777"
separators = number[1::4]
print(separators)


values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
