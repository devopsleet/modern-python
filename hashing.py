from typing import List
from collections import defaultdict
# Two Sum
# def twoSum(nums: List[int], target: int) -> List[int]:
#     hashmap = {}
#     for i in range(len(nums)):
#         num = nums[i]
#         diff = target - num
#         #print(diff)
#         if diff in hashmap:
#             return [i, hashmap[diff]]
#
#         hashmap[num] = i
#     #print(hashmap)
#     return [-1, -1]
#
#
# nums = [2, 7, 11, 15]
# target = 9
# output = twoSum(nums, target)
# print(output)

# Check if the Sentence is Pangram or not

# sentence = "leetcode"
#
# def isPangram(s):
#     for i in range(26):
#         curr_char = chr((ord('a') + i))
#         print(curr_char)
#
#         if sentence.find(curr_char) == -1:
#             return False
#
#
# output = isPangram(sentence)
# print(output)

# arr = [1,1,3,3,5,5,7,7,2,8]


# def countElements(nums):
#     count = 0
#     for num in nums:
#         if num + 1 in nums:
#             count = count + 1
#     return count
#
#
# output = countElements(arr)
# print(output)


arr = [1,3]

losers = defaultdict(int)

for num in arr:
    losers[num] = losers[num]

print(1 in losers)
print(losers)
