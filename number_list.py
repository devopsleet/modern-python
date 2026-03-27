empty_list= []
even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd

print(numbers)
# = list(1,2,3)
third = tuple((3,4,5))
even.extend(odd)
even.extend(third)

print(even)
another_even = even
print(another_even)

even.sort(reverse=True)
print(even)
print(another_even)
print(id(even))
print(id(another_even))


arr = [[1,2], [3,4]]

new_arr = arr.copy()

arr[0].append(5)

print(arr)
print(new_arr)
