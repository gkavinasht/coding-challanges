# 329. Longest Increasing Path in a Matrix
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.
# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

def longestIncreasingPath(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    def dfs(r, c):
        if (r, c) in visited:
            return visited[(r, c)]

        res = 1

        for x, y in [(-1,0),(1,0),(0,-1),(0,1)]:
            rx = r + x
            cy = c + y
            if rx in range(rows) and cy in range(cols) and matrix[rx][cy] > matrix[r][c]:
                res = max(res, 1 + dfs(rx, cy))

        visited[(r, c)] = res
        return visited[(r, c)]

    visited = {}
    res = 0
    rows, cols = len(matrix), len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            path = dfs(row, col)
            res = max(res, path)
            
    return res
    
matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))

# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)