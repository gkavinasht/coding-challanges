# 72. Edit Distance
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character

def minDistance(word1, word2):
    m, n = len(word2), len(word1)

    if m == 0:
        return n
    if n == 0:
        return m

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            left = dp[i - 1][j]
            right = dp[i][j - 1]
            left_down = dp[i - 1][j - 1]

            if word2[i - 1] == word1[j - 1]:
                dp[i][j] = 1 + min(left, right, left_down - 1)
            else:
                dp[i][j] = 1 + min(left, right, left_down)

    return dp[m][n]
 
word1 = "horse"
word2 = "ros"
print(minDistance(word1, word2))

# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
