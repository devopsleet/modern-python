t = ()
print(t)

t = tuple()
print(t)


t = 1,
print(type(t))


t = (1,)
print(t)
print(type(t))


t1 = "a", "b", "c"
print(t1)
t2 = ("a", "b", "c")
print(t2)


# a, b = (1,2)
# i, j = a
# print(i)

# a,b,c,d = (1,2)
#
# print(a)

# unpacking a string
s1, *s2 = "Gagan"
print(s1)
print(type(s1))
print(s2)


t = tuple("Python")
print(t)

l = list("Python")
print(l)

# print(hash(t))

l1 = ['hello world 1212121', 6, 'hello world 1212121']
print(id(l1[0]))
print(id(l1[2]))
l2 = l1


print(id(l1[0]))
print(id(l2[0]))

l1[0] = 2312323223

print(id(l1[0]))
print(id(l2[0]))

new_set = {1,2,3,4,6,4,5}
print(new_set)
# print(sorted(new_set))
print()

s = ["venkyeeeeeeeeeeeeee","venky", "venkyaaaaaaaaaaa"]
s.sort()
print(s)


l = ['9', '10']
print(sorted(l))

l = [9,10]
print(sorted(l))

print(ord('9'))
print(ord('1'))


print(set((0,)))


# new_s = set("Gagan")
# print(new_s)
# print(new_s.reverse())


l2 = list((1,2,3))
print(l2)
print(id(l2))
l2[0] = 10
print(id(l2))


t3 = (1,2,[3,4])
print(id(t3))
t3[2][0] = 10
print(t3)
print(id(t3))


s = {1,2,3}
t = (4,5,6)
s.update(t)
print(s)


s = {1,2,3}
t = (4,5,6)
s.union(t)
print(s.union(t))


s = {"Virat", "Dubey", "Rohit", "Dhoni"}


# Union  ---->  |


a = {1,2,3,4}
b = {2,3,5,7}
c = [10,20,30,40,3]

print(a.intersection(b, c))
print("Set Operations")
result = a & b & c
print(a & b & c)
