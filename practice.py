import collections

str = "eat"

# print(ord(str))
print("".join(sorted(str)))


chars = [1,0,1,0,0]

print(tuple(chars))


print(ord('e') - ord('a'))

dict = collections.defaultdict(list)

dict[(1,0,0)].append('a')
dict[(1,0,0)].append('b')
print(list(dict.keys()))
print(list(dict.values()))
