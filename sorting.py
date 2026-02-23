# quick sort

nums = [1,5,3,2,8,7,6,4]

def quick_sort(nums):

    n = len(nums)
    qsort(nums, 0, n-1)

def qsort(nums,lo,hi):

    if lo < hi:
        p = partition(nums,lo,hi)
        qsort(nums,lo,p-1)
        qsort(nums,p+1, hi)

def partition(nums,lo,hi):
    pivot = nums[hi]
    i = lo
    for j in range(lo,hi):
        if nums[j] < pivot:
            nums[i],nums[j] = nums[j], nums[i]
            i+=1
    nums[i],nums[hi] = nums[hi], nums[i]
    return i

quick_sort(nums)
print(nums)
