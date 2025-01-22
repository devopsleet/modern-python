# string methods

# strip

name = "   Rohit sharma   "

print(name.strip())

new_name = ".a..Rohit Sharma..b."

print(new_name.strip('.aRmb'))


message = "All the best for your GATE 2025 Exam"
print(message.split())

print("how are you doing today?".split(' ', 3))

print(message.split(' ', maxsplit=2))

gate_instructors = "RBR Jay Hari"
print("-".join(gate_instructors))

# join method only works for iterable of strings
# t = [1,2,3,4,5]
# print("#".join(t))


print("#".join("Gagan"))


print(dir(str))
# replace


# count

statement = "Gagan"
print(statement.count('a'))


# find
statement = "Python Course"
print(statement.find("oh"))

l = list()


name = "Virat Kohli"
l = list(name)

print(l)
