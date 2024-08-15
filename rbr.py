from collections import defaultdict

text = "hello world"
char_count = defaultdict(int)

print(char_count)

for char in text:
    char_count[char] += 1

#print(char_count)


build = "gagan"
