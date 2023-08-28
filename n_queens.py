# 51. N-Queens
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

def solveNQueens(n):
    def isValid(row, col):
        # Check the current column in the all the rows
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # Check upper left diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == "Q":
                return False

        # Check upper right diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == "Q":
                return False

        return True

    def solve(row):
        if row == n:
            res.append(["".join(row) for row in board])
            return

        for col in range(n):
            if isValid(row, col):
                board[row][col] = "Q"
                solve(row + 1)
                board[row][col] = "."

    board = [["." for _ in range(n)] for _ in range(n)]
    res = []
    solve(0)
    return res

n = 4
print(solveNQueens(n))

# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Time Complexity: O(n!) -> all the combinations, may be less becuase of backtracking but still exponential
# Space Complexity: O(n**2)