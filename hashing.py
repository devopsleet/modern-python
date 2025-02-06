from typing import List

# Two Sum
def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        num = nums[i]
        diff = target - num
        #print(diff)
        if diff in hashmap:
            return [i, hashmap[diff]]

        hashmap[num] = i
    #print(hashmap)
    return [-1, -1]


nums = [2, 7, 11, 15]
target = 9
output = twoSum(nums, target)
print(output)
