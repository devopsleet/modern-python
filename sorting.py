pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram, key=str.casefold)

print(letters)

numbers = [2.3, 4.5, 6.7]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

names = ["Graham", "John", "terry", "eric", "Terry", "michael"]
names.sort(key=str.casefold)
print(names)
