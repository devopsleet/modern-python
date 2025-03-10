from typing import List

nums = [-1,0,1,2, -1, 4]


def threeSum(nums: List[int], target: int) -> List[List[int]]:
    def twoSum(i):
        #lo = i - 1
        mi = i
        hi = len(nums) - 1

        while mi < hi:
            curr = nums[i-1] + nums[mi] + nums[hi]
            if curr < 0:
                mi = mi + 1
            elif curr > 0:
                hi = hi - 1
            else:
                ans.append([nums[i], nums[mi], nums[hi]])

                mi = mi + 1
                hi = hi - 1
                while mi < hi and nums[mi] == nums[mi-1]:
                    mi = mi + 1

    ans = []

    nums.sort()

    if nums[0] > 0:
        return []
    print(nums)
    for i in range(1,len(nums)):
        if nums[i-1] != nums[i]:
            twoSum(i)
    print(ans)


threeSum(nums, 0)
