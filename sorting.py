nums = [7,9,4,1,3,2,6,5,8]

def selection_sort(nums):

    n = len(nums)

    if n < 2:
        return nums

    # i = 0
    # min_index = i

    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if nums[j] < nums[minIndex]:
                minIndex = j
        nums[minIndex], nums[i] = nums[i], nums[minIndex]

# selection_sort(nums)
# print(nums)


def bubble_sort(nums):

    n = len(nums)

    if n < 2:
        return nums

    Swapped = True
    while Swapped:
        Swapped = False
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                Swapped = True

bubble_sort(nums)
print(nums)
