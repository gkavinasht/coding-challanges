# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

def longestPalindrome(s):
    # Dynamic Programming
    n = len(s)
    # Create a table to store whether a substring is a palindrome
    dp = [[False for _ in range(n)] for _ in range(n)]
    # ans to store first and last indexes of the longest palindrome string
    ans = [0, 0]

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            ans = [i, i + 1]

    # Check for palindromes of length 3 or more
    for diff in range(2, n):
        for i in range(n - diff):
            j = i + diff
            # Check if the current substring is a palindrome
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                ans = [i, j]

    # Extract and return the longest palindromic substring
    i, j = ans
    return s[i:j + 1]

    # Time Complexity: O(n**2)
    # Space Complexity: O(n**2)

    # Check all Substrings - Brute Force
    # def check(i, j):
    #     left, right = i, j - 1

    #     while left < right:
    #         if s[left] != s[right]:
    #             return False
            
    #         left += 1
    #         right -= 1
    #     return True

    # for length in range(len(s), 0, -1):
    #     for start in range(len(s) - length + 1):
    #         if check(start, start + length):
    #             return s[start:start + length]
    # return ""

    # Time Complexity: O(n**3)
    # Space Complexity: O(1)

s = "babad"
print(longestPalindrome(s))

# Output: "bab"
# Explanation: "aba" is also a valid answer.