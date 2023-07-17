# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(s):
    stack = []
    mapping = {"(": ")", "{": "}", "[": "]"}

    for char in s:
        if char in mapping:
            stack.append(char)
        elif stack and char == mapping[stack[-1]]:
            stack.pop()
        else:
            return False

    return len(stack) == 0

s = "()[]{}"
print(isValid(s))

# Time Complexity: O(n)
# Space Complexity: O(n)
# Output: true