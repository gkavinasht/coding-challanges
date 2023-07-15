# 200. Number of Islands
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

from collections import deque

def numIslands(grid):
    if grid is None or len(grid) == 0:
        return 0

    # Using BFS and Queues
    def getIsland(row, col):
        queue = deque([(row, col)])
        visited.add((row, col))

        while queue:
            curr_row, curr_col = queue.popleft()

            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                rx, cy = curr_row + x, curr_col + y

                if rx in range(m) and cy in range(n) and grid[rx][cy] == '1' and (rx, cy) not in visited:
                    queue.append((rx, cy))
                    visited.add((rx, cy))

        return 1

    # Using DFS and Recursion
    # def getIsland(r, c):
    #     if r not in range(m) or c not in range(n) or grid[r][c] == '0' or (r, c) in visited:
    #         return 0

    #     visited.add((r, c))

    #     getIsland(r + 1, c)
    #     getIsland(r - 1, c)
    #     getIsland(r, c + 1)
    #     getIsland(r, c - 1)

    #     return 1

    m = len(grid)
    n = len(grid[0])
    numOfIslands = 0
    visited = set()
    for row in range(m):
        for col in range(n):
            if grid[row][col] == '1' and (row, col) not in visited:
                numOfIslands += getIsland(row, col)

    return numOfIslands

grid = [["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]]
print(numIslands(grid))

# Time Complexity: O(m * n)
# Space Complexity: O(m * n) -> visited and queues/recursion 

# Output: 1