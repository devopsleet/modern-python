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


# While loop
