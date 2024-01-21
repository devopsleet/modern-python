pangram = "The quick brown fox jumps over the lazy dog"

letter = sorted(pangram)

print(letter)

# numbers = [2.3, 4.5, 7.8, 9.8, 1.6]
#
# sorted_numbers = sorted(numbers)
#
# print(sorted_numbers)
# print(numbers)


missing_letter = sorted("The quick brown fox jumps over the lazy dog", key = str.casefold)
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Gagan"
         ]

names.sort(key= str.casefold)
print(names)
