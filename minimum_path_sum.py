# 64. Minimum Path Sum
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

def minPathSum(grid):
    if not grid or len(grid) == 0:
        return 0
    
    m = len(grid)
    n = len(grid[0])
    
    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0:
                dp[i][j] = grid[i][j] + dp[i][j - 1]
            elif j == 0:
                dp[i][j] = grid[i][j] + dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])
    return dp[m - 1][n- 1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))

# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)