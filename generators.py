import sys


def my_range(n: int):
    print("my_range starts now")
    start = 0
    while start < n:
        print(f"my_range is returning {start}")
        yield start
        start += 1


big_range = my_range(5)

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big range
big_list = []
#_ = input("line 19")
for val in big_range:
    _ = input("line 21 inside loop")
    big_list.append(val)


print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(f"big_range {big_range}")
print(f"big list {big_list}")


nums = [1, 2, 3, 4]
print(type(nums))
iterable = iter(nums)

print(type(iterable))
print(next(iterable))


for num in iter(nums):
    print(num)
