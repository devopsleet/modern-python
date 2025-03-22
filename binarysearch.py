# Find an upper bound


#nums = [-7,-4, -1, 0,3,9,12]
nums = [9,9,9,9,9,9,9]
target = 9

# instead of finding the exact location of the target, look for the position to insert the target
def bs_upper_bound(nums, target) -> int:
    l = 0
    r = len(nums)


    while l < r:
        mid = (l+r) // 2

        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] == target:
            l = mid + 1
        else:
            r = mid


    if l > 0 and nums[l-1] == target:
        return l-1
    else:
        return -1

res = bs_upper_bound(nums,target)
print(res)

# find a lower bound

def bs_lower_bound(nums, target)-> int:
    l = 0
    r = len(nums)

    while l < r:
        mid = (l + r) // 2

        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] == target:
            r = mid
        else:
            r = mid

    return l

    # if l < len(nums) and nums[l] == target:
    #     return l
    # else:
    #     return -1

res = bs_lower_bound(nums, target)
print(res)
