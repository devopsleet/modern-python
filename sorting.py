# Quick Sort

from typing import List

nums = [5,1,1,2,0,0]

def quickSort(nums: List[int], p: int, r: int):
    if p < r:
        q = partition(nums,p,r)
        quickSort(nums,p,q-1)
        quickSort(nums,q+1,r)

def partition(nums: List[int], p:int, r:int):
    pivot = nums[r]

    i = p-1
    for j in range(p,r):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i+1

quickSort(nums, 0, len(nums) -1)
print(nums)
