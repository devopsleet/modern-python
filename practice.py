class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def heapify_top_down(n, i):
            largest = i

            lc = (2 * i) + 1
            rc = (2 * i) + 2

            if lc < n and nums[lc] > nums[largest]:
                largest = lc
            if rc < n and nums[rc] > nums[largest]:
                largest = rc

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify_top_down(n, largest)

        def  heap_sort():

            n = len(nums)

            for i in range(n//2-1, -1, -1):
                heapify_top_down(n, i)

            for i in range(n-1,0,-1):
                nums[i], nums[0] = nums[0], nums[i]
                heapify_top_down(i,0)

        heap_sort()
        return nums
