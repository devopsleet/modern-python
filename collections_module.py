from collections import Counter, defaultdict

# From a list

c1 = Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print(c1)


# From a string
c2 = Counter("GaganSingla")
print(c2)


# Accessing counts
print(c1['b'])
print(c1['z'])

c3 = Counter([1,2,3,4,3,2])
c3.update("Gagan")
c3.update([2,3,4])
print(c3)

s = "eceba"
d = defaultdict(int)

print(len(d))

new_dict = {
    "e": 0
}

print(len(new_dict))
