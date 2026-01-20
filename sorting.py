from typing import List

nums = [8,7,6,5,4,3,2,1]

def selection_sort(nums: List[int]) -> None:

    n = len(nums)
    if n < 2:
        return None

    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if nums[j] < nums[min_idx]:
                min = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    print(nums)


selection_sort(nums)
print(nums)
