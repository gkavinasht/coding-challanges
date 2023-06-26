# Implement strStr()
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(haystack, needle):
    if needle == "":
        return 0
    
    if len(haystack) < len(needle):
        return -1
    
    i, j, index = 0, 0, 0
    while i < len(haystack) and j < len(needle):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            i = index + 1
            j = 0
            index = i
            
    return index if j == len(needle) else -1

    # Time Complexity: O(m + n)
	# Space Complexity: O(1)

    # return haystack.find(needle)

    # Time Complexity: O(m * n)
	# Space Complexity: O(1)

haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))

# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.