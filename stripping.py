def removesuffix(string: str, suffix: str) -> str:
    if suffix and string.endswith(suffix):
        return string[:-len(suffix)]
    else:
        return string[:]


filename = 'Jabberwocky.txt'

with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)


# chars = "'Twasebv"
# no_apostrophe = first.strip(chars)
# print(no_apostrophe)

twas_removed = first.removeprefix("'Twas")
print(twas_removed)
toves_removed = removesuffix(first, "toves")
print(toves_removed)
