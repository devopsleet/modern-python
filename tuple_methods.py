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
