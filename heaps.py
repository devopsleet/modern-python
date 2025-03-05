from heapq import *
from graphviz import Digraph
import os
print(os.environ.get('GRAPHVIZ_DOT'))

heap = []

heappush(heap, 1)
heappush(heap,2)
heappush(heap,3)


print(heap[0])

heappop(heap)

print(len(heap))

nums = [43,2,13,634,120]

print(heap)


def visualize_heap(heap):
    graph = Digraph(format='png')

    for i in range(len(heap)):
        graph.node(str(i), str(heap[i]))  # Create nodes

        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < len(heap):
            graph.edge(str(i), str(left_child))  # Left child

        if right_child < len(heap):
            graph.edge(str(i), str(right_child))  # Right child

    # file_path = 'heap_visual.png'
    # if os.path.exists(file_path):
    #     print('yes')
    #     os.remove(file_path)

    graph.render('heap_visual')  # Save and render the graph


heap = [10, 20, 30, 40]

visualize_heap(heap)
