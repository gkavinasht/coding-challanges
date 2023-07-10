# 36. Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

def isValidSudoku(board):
    rows  = [{} for _ in range(9)]
    cols = [{} for _ in range(9)]
    boxes = [{} for _ in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                num = int(num)
                box_index = (i // 3) * 3 + j // 3

                rows[i][num] = rows[i].get(num, 0) + 1
                cols[j][num] = cols[j].get(num, 0) + 1
                boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_index][num] > 1:
                    return False
    return True

board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))

# Time Complexity: O(1) -> as 9x9 is fixed
# Space Complexity: O(1) -> as 9x9 is fixed

# Output: true