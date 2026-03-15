# merge sort

from typing import List

#nums = [5,1,1,2,0,0]

def mergeSort(nums: List[int], p: int, r: int)-> List[int]:

    if p < r:
        q = (p+r)//2
        mergeSort(nums, p,q)
        mergeSort(nums,q+1,r)
        merge(nums,p,q,r)

def merge(nums,p,q,r):
    n1 = q-p + 1
    n2 = r-q

    list1 = [0] * (n1+1)

    for i in range(n1):
        list1[i] = nums[p+i]

    list1[-1] = float('inf')

    list2 = [0] * (n2+1)

    for i in range(n2):
        list2[i] = nums[q+i+1]

    list2[-1] = float('inf')

    i = j = 0

    for k in range(p,r+1):
        if list1[i] <= list2[j]:
            nums[k] = list1[i]
            i += 1
        else:
            nums[k] = list2[j]
            j += 1

mergeSort(nums,0, len(nums)-1)
print(nums)
