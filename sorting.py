from typing import List

nums = [8,7,6,5,4,3,2,1]

def SortArray(nums):

    p = 0
    r = len(nums) - 1

    mergeSort(nums,p,r)

def mergeSort(nums, p, r):

    if p < r:
        q = (p+r)//2

        mergeSort(nums,p, q)
        mergeSort(nums, q+1,r)
        merge(nums,p,q,r)

def merge(nums,p,q,r):

    n1 = q-p + 1
    n2 = r-q+1

    arr1 = []
    for i in range(n1):
        arr1.append(nums[i])

    arr1.append(float('inf'))

    arr2 = []
    for j in range(n2):
        arr2.append(nums[j])
    arr2.append(float('inf'))

    ans = []
    for k in range(p,r-1)
