print("Today is a good day to learn Python")
print('Python is fun')
print("We can even include 'quotes'")
greeting = "Hello"
name = "Gagan"
print(greeting + name)

# if we want a space, we cana dd that too
print(greeting + ' ' + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

# age = "2 years"
print(name + " is " + str(age) + " years old")
print(type(age))
print(2.4)


print(2.5)
print(2.6)
print(2.7)

print(2.8)
print(10 << 2)


# membership operator

players = ["kohli", "ponting"]

print("kohli")


k = set((1,2,3,4,5))
#m = set('a', 'b')
print( 2 in k)

# user_input = input("Enter Something")
#
# print(user_input)
#
# # identity operators
# rupees = int(input("Money from father"))
# print(rupees)
# if rupees >= 80:
#     print("Buy")


marks = 92

if marks >= 90:
    print("Grade S")




a,b,c = 10,12,5
print(a,b, c)



x,y,z = 10,5,-2

if x > 5:
    x = x >> y // ~z
    if x > 12:
        print(x)
    else:
        print(y)

# Loops
routine = ["a", "b", "c"]

match_tom = "India vs Pakistan"

for c  in match_tom:
    print(c)

players = ["Bradman", "Sachin", "Kohli", "Richards"]

for i in range(len(players)-1, -2, -1):
    print(players[i])

print()
for i in range(-len(players), 0):
    print(players[i])

for i,name in enumerate(players):
    print(i, name)


election_parties = ["bjp", "congress"]

constituency = [240, 120]

for party, value in zip(election_parties, constituency):
    print(party, value)

l1 = ["a", "b", "c"]
l2 = [1,2,3]
l3 = {1, True, 1.0}

for a,b,c in zip(l1,l2,l3):
    print(a,b,c)


# concatenate operators

print('RCB' + 'CSK')


# string repetition operator

print("Python " * 2)
print("Python" * 0)


# string comparison operator
print("Venky" == "Venky")
print("Venky" != "venky")

print("Venky" > "venky")


# membership operator

print("Ven" in "Venky")


# Escape sequence
print("Today's match is \"India vs Pakistan\"")


# \n - new line
print("Match 1\nMatch2\n")

print("Hello World! \b")
print("Hello\b")
print("Hello \b World")

print("Venkat\besh\b")


# \ooo

print('\141')

print('\141\142')
print('\1412')


# xhh
print('\x65')

#print('\x')

# string formatting operator
subject = "Python"
print("%s class is happening today"%subject)

# print("I'm Gagan and my age is 31")

name = "Gagan"
age = 31
print("I'm %s and my age is %d"   %(name, age))

print(f"I'm {name} and my age is {age}")

print("I'm {0} and my age is {1}".format(name, age))

dict = {"name": "Gagan",
        "age": 31}
print("I'm {name} and my age is {age}".format(**dict))

name = "Gagan"
city = "Dallas"

print("%s %s"%(city, name))

score = 12.787

print("Score is %s" %score)

info = "I'm Venkatesh"

info[5:10]
print(info[5:])
print(info[:])
print(info[::])

# string methods

str = "Hello World"
str2 = "HELLO WORLD"

# Case conversion methods

# 1. lower()
print(str.lower())
print(str2.lower())

# 2. upper()
print(str.upper())
print(str.upper())

# 3. capitalize()
print(str.capitalize())
print(str2.capitalize())

# 4. title()
print(str.title())
print(str2.title())

# 5. swapcase()
print(str.swapcase())
print(str2.swapcase())

# Whitespace and padding methods`

# 1. strip()

str = "hello" \
      "" \
      "world"

str2 = """ 

Hello 

World

"""

str3 = "\n\thello   \n\t World"
print(str)
print(str.strip())
print(str2)
print(str2.strip())
print(str3)
print(str3.strip())

str4 = "----hello--- world---------"
print(str4.strip('-'))


# 2. lstrip()

str5 = "        $$$$$$$$$$-----------hello"
print(str5.lstrip())
print(str5.lstrip('$'))


# 3. rstrip()

str6 = "World$$$$$$$$$$$$$$$$$$$$$$$$$$      "
print(str6.rstrip())
print(str6.rstrip('$'))

# 4. zfill()

str6 = "42"
str7 = "+43"

print(str6.zfill(2))
print(str7.zfill(4))

# 5. str.center(width, fillchar = ' ')

str8  = "hi"
print(str8.center(8, "-"))


# 6.ljust(width, fillchar= ' ')

str9 = "hi"

print(str9.ljust(5, '-'))


# 7 rjust(width, fillchar= " ")

str10 = "world"

print(str10.rjust(7, "1"))
