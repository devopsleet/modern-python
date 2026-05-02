# all tha alphabets
pangram = "The quick brown fox jumps over the lazy dog"


letter = sorted(pangram)

print(letter)
numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)


another_sorted_numbers = numbers.sort()
print(numbers)


print(another_sorted_numbers)
missing_letter = sorted("The quick brown fox jumps over the lazy dog", key=str.casefold)
print(missing_letter)


names = ["Graham", "John", "terry", "eric", "Terry", "michael"]

names.sort()

print(names)
