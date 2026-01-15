nums = [1,5,3,2,8,7,6,4]



def merge_sort(nums):
    n = len(nums)

    if n <= 1:
        return nums

    pivot = int(len(nums)/2)
    left_list = merge_sort(nums[0:pivot])
    right_list = merge_sort(nums[pivot:])

    return merge(left_list, right_list)


def merge(ll,rl):
    left_cursor = right_cursor = 0

    ans = []

    while left_curosr < len(ll) and
