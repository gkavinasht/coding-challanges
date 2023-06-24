# 54. Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.

def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []

    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse top row from left to right
        for col in range(left, right + 1):
            res.append(matrix[top][col])
        top += 1

        # Traverse right column from top to bottom
        for row in range(top, bottom + 1):
            res.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left-1, -1):
                res.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top-1, -1):
                res.append(matrix[row][left])
            left += 1 
    return res

    # Time Complexity: O(m * n)
	# Space Complexity: O(1)
    
    # m = len(matrix)
    # n = len(matrix[0])
    # res = []
    # seen = [[False]*n for _ in range(m)]
    
    # drc = [(0,1),(1,0),(0,-1),(-1,0)]
    # direction = 0
    
    # r,c = 0,0
    # for i in range(m*n):
    #     res.append(matrix[r][c])
    #     seen[r][c] = True
        
    #     if i == m*n -1:
    #         return res
    #     nr, nc = r + drc[direction][0], c + drc[direction][1]
    #     if 0<=nr<m and 0<=nc<n and not seen[nr][nc]:
    #         r, c = nr, nc
    #     else:
    #         direction = (direction + 1) % 4
    #         r, c = r + drc[direction][0], c+ drc[direction][1]
    
    # return res

    # Time Complexity: O(m * n)
	# Space Complexity: O(m * n)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))

# Output: [1,2,3,6,9,8,7,4,5]