from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            difference = target - num
            if difference in dic:
                return [i, dic[difference]]

        dic[num] = i
