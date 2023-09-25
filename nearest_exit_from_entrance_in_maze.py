# 1926. Nearest Exit from Entrance in Maze
# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.
# In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.
# Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

import collections
def nearestExit(maze, entrance):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    queue = collections.deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
    visited = set()
    visited.add((entrance[0], entrance[1]))
    
    while queue:
        row, col, steps = queue.popleft()
        
        if (row != entrance[0] or col != entrance[1]) and (row == 0 or row == rows - 1 or col == 0 or col == cols - 1):
            return steps
        
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols and maze[r][c] == '.' and (r, c) not in visited:
                visited.add((r, c))  # Mark the cell as visited
                queue.append((r, c, steps + 1))

    return -1

maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [1,2]
print(nearestExit(maze, entrance))

# Output: 1
# Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
# Initially, you are at the entrance cell [1,2].
# - You can reach [1,0] by moving 2 steps left.
# - You can reach [0,2] by moving 1 step up.
# It is impossible to reach [2,3] from the entrance.
# Thus, the nearest exit is [0,2], which is 1 step away.