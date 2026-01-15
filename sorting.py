# Selection Sort

nums = [7,3,2,5,6,10,9,8,1]

def selection_sort(nums):
     n = len(nums)

     if n == 1:
         return nums

     curr = 0

     for i in range(1,n):
         min_element = min(nums[:])
         nums[curr],
