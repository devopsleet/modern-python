range_val = range(5)

print(range_val)
print(type(range_val))
print(id(range))

print(list(range_val))

print("New Range")
range_val2 = range(10,15)
print(range(10,15))

print(list(range(10,15,2)))


print(list(range(-5)))


print(list(range(-5, 0)))


print(list(range(0,-5,-1)))


#set_3 = set(1,2,3)

print("")
#print(set_3)

set_1 = {1,2,3,4,5}
set_2 = set((1,2,3,4,5))
print(set_2)


set_3 = {1,1.0, True,2.0,2,3,4,5,6}
print(set_3)


set_3.add("Virat")
print(set_3)

a = False
print(type(a))


print(False == 0)
print(True == 2)

set_5 = {"Virat", "123", 1, "1", True, False, 0}
print(set_5)


print(1.0 == 1 == True)

set_a = {'A', 'B'}

l = ['a', 'b', 'VIRAT']
l[2] = 'KOHLI'
print(l)

set_6 = {'KOHLI'}
set_6.remove('KOHLI')
print(set_6)


set_b = {"1", "2", 1,2}

print(id(set_b))
#print(hash(set_b))

#set_b.add(['a', 'b'])

l.append({'a'})

print(l)


print(hash(1))
print(hash(1.0))

print(hash(2))
print(hash(2.0))
print(hash('2'))


set_c = {1,2,3,('A', 'B')}
print(set_c)


set_d = {1,2,'w', 'd'}
print(set_d)

set_1 = set(('1',1))
print(set_1)
print(type(set_1))

f_set_1 = frozenset({'1', 1})
print(f_set_1)
print(type(f_set_1))

rcb_batter_scores = {"Virat": 55,
                     "faf": 20,
                     "Green": 20,
                     "Maxi": 20
                     }

print(rcb_batter_scores)
print(id(rcb_batter_scores))
rcb_batter_scores.update({"DK": 35})
print(id(rcb_batter_scores))


aus_batter_scores = {"Warner" : 75, "Head" : 100, "Maxi": 1}

# dict_a = {"Virat" : [56,23,234],
#           "Rohit" : [23[4,5,6,6,6]]}


# Boolan Data types

print(id(bool(False)))
print(id(bool(0.0)))
print(id(bool(None)))
print(id(bool('')))
f = (2 == 3)
print(id(f))

print(bool('0'))
print(bool(" "))

from decimal import Decimal

print(Decimal('0.1'))
