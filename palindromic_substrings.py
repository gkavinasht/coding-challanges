# 647. Palindromic Substrings
# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

def countSubstrings(s):
    n = len(s)
    count = 0
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    # i - start of a string, j - end of a string
    for j in range(n):
        count += 1
        for i in range(j):
            # s[i:j] is a plaindrome
            # if s[i] == s[j] and j - i == 1 (2-length string plaindrome)
            # if s[i] == s[j] and s[i + 1:j - 1] is also a palindrome
            if s[i] == s[j] and (dp[i + 1][j - 1] or j - i == 1):
                dp[i][j] = True
                count += 1
    return count

s = "abc"
print(countSubstrings(s))
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Time Complexity: O(n**2)
# Space Complexity: O(n**2)