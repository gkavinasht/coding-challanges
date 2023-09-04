# 32. Longest Valid Parentheses
# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring

import collections
def longestValidParentheses(s):
    max_len = 0
    i = 0
    n = len(s)
    stack = collections.deque([-1])

    while i < n:
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
        i += 1

    return max_len

s = "(()"
print(longestValidParentheses(s))

# Output: 2
# Explanation: The longest valid parentheses substring is "()".

# Time Complexity: O(n)
# Space Complexity: O(n)