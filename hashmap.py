mp = {}

mp['a'] = 0
mp['b'] = 1

print(mp.keys())
print(mp)

mp.setdefault('c', 3)

print(mp)
r = mp.get('d', 4)

print(r)

print(mp.popitem())
print(mp)



keys = ['a', 'b', 'c']

mp = dict.fromkeys(keys)
mp = dict.fromkeys(keys, 1)
print(mp)
