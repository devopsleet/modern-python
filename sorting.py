pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)

print(letters)

missing_letters = sorted("The quick brown fox jumped over the lazy dog",
                         key=str.casefold)
print(missing_letters)

numbers = [2.3,4.5,8.7,3.1,9.2]

sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)

new_list = ['T', 'h', 'e']
new_list.sort(key=str.casefold)

print(new_list)
