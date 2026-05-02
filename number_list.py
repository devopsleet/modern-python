import copy

empty_list = []

even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd
print(numbers)


sorted_numbers = sorted(numbers)
print(sorted_numbers)

print(numbers)


digits = list("432985617")
print(digits)


# more_numbers = list(numbers)
# print(more_numbers)
#
# print(numbers is more_numbers)
# print(numbers == more_numbers)

# more_numbers = numbers[:]
# print(more_numbers is numbers)
# more_numbers.append(10)
# print(f"More numbers is {more_numbers}")
# print(f"Original list is {numbers}")

l1 = [[1,2], [3,4]]
# l2 = l1[:]
# print(l1 is l2)

# l1[0].append(5)
l2 = copy.deepcopy(l1)
print(l2)
l2.append(10)
print(l1)
print(l2)
print(l1 is l2)
