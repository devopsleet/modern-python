filename = 'D:/Python/jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

chars = "'Twas"
no_apos = first.strip(chars)
print(no_apos)

twas_removed = first.removeprefix("'Twas")
