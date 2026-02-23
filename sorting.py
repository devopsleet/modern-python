# merge sort

nums = [1,5,3,2,8,7,6,4]

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = int(len(nums)/2)
    p = merge_sort(nums[0:pivot])
    q = merge_sort(nums[pivot:])
    return merge(p,q)

def merge(p,q):
    left = right = 0

    ans = []

    while left < len(p) and right < len(q):
        if p[left] < q[right]:
            ans.append(p[left])
            left += 1
        else:
            ans.append(q[right])
            right += 1

    ans.extend(p[left:])
    ans.extend(q[right:])

    return ans

answer = merge_sort(nums)
print(answer)
