empty_list = []

even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]
numbers = [even , odd]

print(numbers)


for number_lists in numbers:
    print(number_lists)

    for value in number_lists:
        print(value)
# sorted_numbers = sorted(numbers)
#
# print(sorted_numbers)
# print(numbers)
# print(numbers.sort())
#
# digits = list("4321896")
# print(digits)
# even.extend(odd)
# print(even)
# another_even = even
# print(another_even)
# even.sort(reverse=True)
# print(even)
# print(another_even)
