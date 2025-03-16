s = "abcde"

length = len(s)

for _ in range(length):
    s = s[1:] + s[0]
    print(s)
