# QuickSort Algorithm

nums = [1,5,3,2,8,7,6,4]

from typing import List
import random
class Solution:
    def quicksort(self, nums: List[int]):

        n = len(nums)
        self.qSort(nums,0, n-1)


    def qSort(self,nums: List[int],lo:int, hi:int):

        if lo < hi:
            p = self.partition(nums, lo, hi)
            self.qSort(nums,lo, p-1)
            self.qSort(nums,p+1, hi)


    def partition(self, nums, lo, hi):

        pivot_idx = random.randint(lo, hi)
        nums[hi], nums[pivot_idx] = nums[pivot_idx], nums[hi]

        pivot = nums[hi]
        i = lo
        for j in range(lo, hi):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[hi] = nums[hi], nums[i]
        return i


S = Solution()
S.quicksort(nums)
print(nums)
