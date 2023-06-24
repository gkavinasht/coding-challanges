# 498. Diagonal Traverse
# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

def findDiagonalOrder(mat):
    if mat is None or len(mat) == 0:
        return []

    m = len(mat)
    n = len(mat[0])
    total = m * n

    i, j, k = 0, 0, 0
    res = []
    up = True

    while k < total:
        res.append(mat[i][j])

        if up:
            if i == 0 and j < n - 1:
                j += 1
                up = not up
            elif j == n - 1:
                i += 1
                up = not up
            else:
                i -= 1
                j += 1
        else:
            if i < m - 1 and j == 0:
                i += 1
                up = not up
            elif i == m - 1:
                j += 1
                up = not up
            else:
                i += 1
                j -= 1

        k += 1
    return res

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(findDiagonalOrder(mat))

# Time Complexity: O(m * n)
# Space Complexity: O(1)

# Output: [1,2,4,7,5,3,6,8,9]