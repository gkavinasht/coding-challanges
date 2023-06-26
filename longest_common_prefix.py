# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def longestCommonPrefix(strs):
    prefix = ""
    if strs is None:
        return prefix

    length = len(min(strs))
    for i in range(length):
        count = 0
        for j in range(1, len(strs)):
            if strs[j][i] == strs[j-1][i]:
                count += 1
        if count == len(strs) - 1:
            prefix += strs[0][i]
        else:
            break
    return prefix

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))

# Time Complexity: O(m * n)
# Space Complexity: O(1)

# Output: "fl"