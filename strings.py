# concatenate operator

print('RCB ' + 'CSK')
print("RCB" + "VS" + "CSK")


print("Python" * 2)
print("python" * 5)


print("Python" * 0)


print("Python" * -1)


print(5* "Python")


# String Comparison Operator
print("Venky" == "Venky")


print("Venky" <= "Venky")

print("Venky" != "venky")

print("Venky" <= "venky")


print("Gagan" >= "gagan")
print("Gagan" >= "gagan")

print(ord("g"))
print(ord("G"))

print("Venky" > "Venkateeeeeeeeeeeeeeeeeeeee")

print(ord('a'))
print(ord('y'))


# Membership operator

print("Ven" in "Venky")
print("Ven" not in "Venky")


# Escape sequence

print("Today's Match:\"India vs Pakistan\"")
print('Today\'s Match')

print("Match 1: Afghanistan \nMatch 2: India")

# \b acts as a backspace
print("Venkatesh\b")
print("Hello\b World!")
print("Ga\bga\bn")


# \ooo

print('\141')
print('\14123')

print("\x65")


# String formatting operator
subject = "Python"
print(f"{subject} class is happening today")
print("%s class is happening today" % subject)

name = "Gagan"
city = "Dallas"
print("I'm %s  and I live in %s" % (name, city))

score = 12.5
print("Score is %f" % score)

score = 12.1
print("score is %d"%score)


print("Gagan" + str(23))

age = 23
print("Gagan%s" % age)

info = "I'm Venkatesh and I work as a Software Engineer"

print(info[5:10])

full_name = "Venkatesh Elangovan"
print(full_name[5:9:2])
print(full_name[10:])
print(full_name[:10])
print(full_name[:])
print(full_name[::2])
print("New String")
print(full_name[15:10:-1])

print(full_name[5: 18: 202])
print(full_name[::-1])


v = "madam"
v2 = "MadaM"
print(v == v[::-1])

print(v[::-1])
print(v[::-1][::-1])


print(full_name[11: -12: -1])


name = "Venky"
age = 26

print("My name is %s and I am %d years old" %(name, age))
