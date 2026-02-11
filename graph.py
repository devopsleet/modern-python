# calculate number of islands

from typing import List

grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

def number_of_islands(grid: List[List[str]])->int:

    def isValid(a,b):
        return 0 <= a < m and 0 <= b < n and grid[a][b] == "1"
    def dfs(start_row, start_col):
        for x,y in directions:
            new_x, new_y = start_row + x, start_col+ y
            if isValid(new_x, new_y) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                dfs(new_x, new_y)


    # calculate number of rows
    m = len(grid)
    # calculate number of columns
    n = len(grid[0])

    # set 4 directions
    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    # set visited array to track visited nodes
    visited = set()

    # answer variable
    ans = 0

    # traverse the grid
    for r in range(m):
        for c in range(n):
            if grid[r][c] =="1" and (r,c) not in visited:
                ans += 1
                visited.add((r,c))
                dfs(r,c)


    return ans


answer = number_of_islands(grid)
print(answer)
