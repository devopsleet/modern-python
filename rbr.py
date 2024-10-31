from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]
#
#
# S = Solution()
# print(S.twoSum([1, 2, 39, 4], 4))


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashMap = {}
#         for i in range(len(nums)):
#             curr = nums[i]
#             if (target - curr) in hashMap:
#                 return [i, hashMap[target - curr]]
#             hashMap[curr] = i
#
#
# S = Solution()
# print(S.twoSum([1, 2, 39, 4], 9))

# my_list = [1, 2, 3, 4, 5]
# reversed_list = reversed(my_list)
# print(reversed_list)  # Output: [5, 4, 3, 2, 1]
# print(my_list)  # Output: [1, 2, 3, 4, 5] (original list is unchanged
#

# def dfs(self, root: Optional[TreeNode])-> int:
#     for i in range(len(s)):


# def longestSubstring(s: str) -> int:
#     left = ans = 0
#     seen = set()
#     for right in range(len(s)):
#         if s[right] not in seen:
#             seen.add(s[right])
#         else:
#             left = right
#
#         ans = max(ans, right - left + 1)
#
#
#     return ans


# def longestSubstring(s: str) -> int:
#     n = len(s)
#     res = 0
#     for i in range(n):
#         for j in range(i, n):
#             if check(i, j, s):
#                 res = max(res, j - i + 1)
#
#     return res
#
#
# def check(start, end, s):
#     checks = set()
#     for i in range(start, end + 1):
#         char = s[i]
#         if char in checks:
#             return False
#         checks.add(char)
#     return True
#
#
# print(longestSubstring("abcabc"))
#
# print("The new software")

#
# class Dog(object):
#     def __init__(self):
#
#
#     def speak(self):
#         pass


from typing import List


class SparseVector:
    def __init__(self, nums:List[int]):
        self.array = []

        for index, num in enumerate(nums):
            if num:
                self.array.append((index, num))

    def dotProduct(self, vec: 'SparseVector') -> int:

        i = j = 0
        dotProduct = 0

        while i < len(self.array) and j < len(vec.array):
            indexi, valuei = self.array[i]
            indexj, valuej = vec.array[j]

            if indexi == indexj:
                dotProduct = dotProduct + (valuei * valuej)
            elif indexi > indexj:
                j = j + 1
            else:
                i = i + 1

        return dotProduct


nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]

v1 = SparseVector(nums1)
v2 = SparseVector(nums2)

the newvalue = value + 10

value =

the
answer = v1.dotProduct(v2)
print(answer)

s-counts.collections

prefix_sum = 0

the a
thevalue
