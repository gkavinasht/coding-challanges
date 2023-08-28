# 74. Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

def searchMatrix(matrix, target):
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    
    left, right = 0, m * n - 1
    while left <= right:
        pivot_index = (left + right) // 2
        pivot_element = matrix[pivot_index // n][pivot_index % n]
        
        if target == pivot_element:
            return True
        else:
            if target < pivot_element:
                right = pivot_index - 1
            else:
                left = pivot_index + 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

print(searchMatrix(matrix, target))

# Time Compelxity: O(log(m * n))
# Space Complexity: O(1)

# Output: true