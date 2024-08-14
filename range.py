# not iterable
range_val = range(5)
print(range_val)
print(type(range_val))


print(list(range_val))

# iterable
range(10, 15)
for i in range(10,15):
    print(i)

range_val3 = range(5)
print(list(range_val3))

# Sets
set_1 = {1,2,3}
print(set_1)
print(type(set_1))


set3 = {1,4,2,2.0, 5.5, "Gagan", "Singla"}
print(set3)

print(2 == 2.0)
print(True == 1)

set_4 = {True, 1, 1.0}
print(set_4)

set5 = {0, False, 0.0}
print(set5)


set_b = {1,2}
#set_b.add([1,2,3,])

# Frozen Set

f_set_1 = frozenset((1,2,1.0))
print(f_set_1)
