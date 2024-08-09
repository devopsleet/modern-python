def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return True
        if current_sum > target:
            right -= 1
        else:
            left += 1
    return False


print(check_for_target([1,3,5,7,9], 8))
