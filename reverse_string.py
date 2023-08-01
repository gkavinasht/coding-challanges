# 344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    # Iterative
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

    # Time Complexity: O(n)
    # Space Complexity: O(1)

    # Recursion
    # def helper(i, j):
    #     if i >= j:
    #         return
            
    #     s[i], s[j] = s[j], s[i]
    #     helper(i + 1, j - 1)

    # helper(0, len(s) - 1)

    # Time Complexity: O(n)
    # Space Complexity: O(n)

s = ["h","e","l","l","o"]
reverseString(s)
print(s)

# Output: ["o","l","l","e","h"]