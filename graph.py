from collections import defaultdict
from typing import List

isConnected = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
]

def calculate_provinces(isConnected: List[List[int]])->int:

    # stack implementation of a neighboring towns

    def dfs(node):
        stack = [node]

        while stack:
            node = stack.pop()

            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        # for neighbor in graph[node]:
        #     if neighbor not in seen:
        #         seen.add(neighbor)
        #         dfs(neighbor)

    # build the graph
    n = len(isConnected)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i+1,n):
            if isConnected[i][j]:
                graph[i].append(j)
                graph[j].append(i)

    # need a set to track the visited nodes
    seen = set()

    ans = 0

    for i in range(n):
        if i not in seen:
            ans += 1
            seen.add(i)
            dfs(i)

    return ans

number_of_province = calculate_provinces(isConnected)
print(number_of_province)
