import re

str = 'an example word:cat!!!!'

match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
    print('found', match.group())
else:
    print('did not find')


print(re.findall(r'a', "cat"))
print(re.findall(r".", "cat"))
print(re.findall(r"\.", "gagan.singla"))

print(re.findall(r"a.b", "a_b a|b a+bc a b"))
print(re.findall(r"a.b", "a_b a1b a b"))

print(re.findall(r'\W+', 'hello world_123!'))
