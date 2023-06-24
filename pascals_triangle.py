# 118. Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

def generate(numRows):
    triangle = []
    for num in range(1, numRows + 1):
        current_row = [1] * num
        if len(current_row) >= 3:
            previous_row = triangle[num - 2]
            for i in range(1, num - 1):
                current_row[i] = previous_row[i - 1] + previous_row[i]
        triangle.append(current_row)
    return triangle

numRows = 5
print(generate(numRows))

# Time Complexity: O(n*2)
# Space Complexity: O(1)

# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]