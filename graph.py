# Calculate the number of provinces
import collections
from typing import List

isConnected = [
     [1,1,0],
     [1,1,0],
     [0,0,1]
]

def calculate_provinces(isConected: List[List[int]])->int:

    def dfs(node):
        for neigbor in graph.get(node, []):
            if neigbor not in seen:
                seen.add(neigbor)
                dfs(neigbor)
    n = len(isConnected)

    graph = {}

    for i in range(n):
        for j in range(i+1,n):
            if isConnected[i][j]:
                graph.setdefault(i,[]).append(j)
                graph.setdefault(j,[]).append(i)

    seen = set()
    ans =0
    for i in range(n):
        if i not in seen:
            ans += 1
            seen.add(i)
            dfs(i)
    return ans

answer = calculate_provinces(isConnected)
print(answer)
