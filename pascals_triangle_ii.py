# 119. Pascal's Triangle II
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

def getRow(rowIndex):
	# Dynamic Programming
    row = [0] * (rowIndex + 1)
    row[0] = 1

    for i in range(1, rowIndex + 1):
        for j in range(i, 0, -1):
            row[j] += row[j-1]

    return row
    
    # row = [1]
    # for i in range(1, rowIndex + 1):
    #     current_row = [1] * (i + 1)
    #     if len(current_row) >= 3:
    #         previous_row = row
    #         for j in range(1, len(current_row) - 1):
    #             current_row[j] = previous_row[j - 1] + previous_row[j]
    #     row = current_row
    # return row

    # Recursion
    # if rowIndex == 0:
    #     return [1] # Base case
    
    # # Recursive call to get the previous row
    # prev = self.getRow(rowIndex-1)
    # # The first element of each row is always 1
    # row = [1]

    # # Generate the middle elements of the row
    # for i in range(1, len(prev)):
    #     row.append(prev[i-1] + prev[i])

    # # The last element of each row is always 1
    # row.append(1)
    # return row

rowIndex = 3
print(getRow(rowIndex))

# Time Complexity: O(n*2)
# Space Complexity: O(n)

# Output: [1,3,3,1]