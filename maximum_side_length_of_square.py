# 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
# Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

def maxSideLength(mat, threshold):
    max_side_length = 0
    rows, cols = len(mat), len(mat[0])

    # Calculate the cumulative sum matrix
    prefix_sum = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
    for i in range(rows):
        for j in range(cols):
            prefix_sum[i + 1][j + 1] = (
                    prefix_sum[i + 1][j] 
                    + prefix_sum[i][j + 1] 
                    - prefix_sum[i][j] 
                    + mat[i][j]
                )

    # Helper function to calculate the sum of a square submatrix
    def getSum(x1, y1, x2, y2):
        return (
            prefix_sum[x2][y2]
            - prefix_sum[x1][y2]
            - prefix_sum[x2][y1]
            + prefix_sum[x1][y1]
        )

    # Binary search for the maximum side length
    left, right = 1, min(rows, cols)
    while left <= right:
        mid = (left + right) // 2
        found = False

        # Check if there exists a submatrix of side length mid with sum <= threshold
        for i in range(rows - mid + 1):
            for j in range(cols - mid + 1):
                if getSum(i, j, i + mid, j + mid) <= threshold:
                    found = True
                    break

        if found:
            max_side_length = mid
            left = mid + 1
        else:
            right = mid - 1

    return max_side_length


mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
threshold = 4
print(maxSideLength(mat, threshold))
# Output: 2
# Explanation: The maximum side length of square with sum less than 4 is 2 as shown.

# Time Complexity: O(m * n * log(min(m, n)))
# Space Complexity: O(m * n)