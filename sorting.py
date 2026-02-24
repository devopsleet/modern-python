from collections import Counter

# nums = [4,5,5,2,1,1,1,5,2,3,3,5,2]
# k = 3


nums = [4,5,5,2,1,1,1,5,2,3,3,5,2]


count = Counter(nums)

print(count)
unique = list(count.keys())
print(unique)
k = 3

def quick_select(unique, k):

    n = len(unique)

    left = 0
    right = n - 1
