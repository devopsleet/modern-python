from heapq import *
from graphviz import Digraph
# import os
# print(os.environ.get('GRAPHVIZ_DOT'))
#
# heap = []
#
# heappush(heap, 1)
# heappush(heap,2)
# heappush(heap,3)
#
#
# print(heap[0])
#
# heappop(heap)
#
# print(len(heap))

# nums = [43,2,13,634,120]
#
# for i in nums:
#     num = num * -1
#
# print(nums)

#print(heap)


# def visualize_heap(heap):
#     graph = Digraph(format='png')
#
#     for i in range(len(heap)):
#         graph.node(str(i), str(heap[i]))  # Create nodes
#
#         left_child = 2 * i + 1
#         right_child = 2 * i + 2
#
#         if left_child < len(heap):
#             graph.edge(str(i), str(left_child))  # Left child
#
#         if right_child < len(heap):
#             graph.edge(str(i), str(right_child))  # Right child
#
#     # file_path = 'heap_visual.png'
#     # if os.path.exists(file_path):
#     #     print('yes')
#     #     os.remove(file_path)
#
#     graph.render('heap_visual')  # Save and render the graph
#
#
# heap = [10, 20, 30, 40]
#
# visualize_heap(heap)

import heapq
from typing import List


def medianSlidingWindow(nums: List[int], k: int) -> List[float]:
    def calculate_median(arr):
        print(arr)
        heapq.heapify(arr)
        arr = [heapq.heappop(arr) for _ in range(len(arr))]
        print(arr)
        median = 0.0
        left = 0
        right = len(arr) - 1
        while left < right:
            left = left + 1
            right = right - 1

        # print(left)
        # print(right)
        # print(arr)
        if left == right:
            median = float(arr[left])
        else:
            median = (arr[left] + arr[right]) /2
        # print(median)
        return median

    n = len(nums)
    if k == 1:
        return [float(num) for num in nums]

    ans = []

    left = 0
    right = k - 1

    while right < n:
        median = calculate_median(nums[left:right+ 1])
        ans.append(median)
        left = left + 1
        right = right + 1

    return ans


res = medianSlidingWindow([1,3,-1], 3)
print(res)
