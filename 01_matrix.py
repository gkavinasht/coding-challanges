# 542. 01 Matrix
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.

import collections
def updateMatrix(matrix):
	rows = len(matrix)
	cols = len(matrix[0])
	queue = collections.deque()
	visited = set()            

	for row in range(rows):
	    for col in range(cols):
	        if matrix[row][col] == 0:
	            queue.append((row, col, 0))
	            visited.add((row, col))

	while queue:
	    m, n, s = queue.popleft()

	    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
	        rx, cy = m + x, n + y
	        if (rx, cy) not in visited and rx in range(rows) and cy in range(cols):
	            visited.add((rx, cy))
	            queue.append([rx, cy, s + 1])
	            matrix[rx][cy] = s + 1
	return matrix

    # rows = len(matrix)
    # cols = len(matrix[0])

    # def getDistance(r, c):
    #     queue = [[r, c, 0]]
    #     visited = set()
        
    #     while queue:
    #         m, n, s = queue.pop(0)

    #         if matrix[m][n] == 0:
    #             matrix[r][c] = s
    #             return 0

    #         for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    #             rx, cy = m + x, n + y
    #             if (rx, cy) not in visited and rx in range(rows) and cy in range(cols):
    #                 visited.add((rx, cy))
    #                 queue.append([rx, cy, s + 1])

    # for row in range(rows):
    #     for col in range(cols):
    #         if matrix[row][col] == 1:
    #             getDistance(row, col)
    # return matrix

mat = [[0,0,0],[0,1,0],[0,0,0]]
print(updateMatrix(mat))

# Time Complexity: O(mn)
# Space Complexity: O(mn)
# Output: [[0,0,0],[0,1,0],[0,0,0]]