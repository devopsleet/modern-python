from typing import List
def flip(nums:str)-> int:
    l = 0
    count = 0
    ans = 0

    for r in range(len(nums)):
        if nums[r] == "0":
            count = count + 1

        while count > 1  and l < len(nums):
            if nums[l] == "0":
                count = count - 1
            l += 1

        ans = max(ans, r - l + 1)

    return ans

ans = flip("1111100111")
print(ans)
