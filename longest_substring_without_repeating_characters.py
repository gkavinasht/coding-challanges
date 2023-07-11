# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s):
    i, j = 0, 0
    max_length = 0
    curr = []

    while j < len(s):
        if s[j] not in curr:
            curr.append(s[j])
            max_length = max(max_length, len(curr))
            j += 1
        else:
            curr.remove(s[i])
            i += 1
    return max_length

s = "abcabcbb"
print(lengthOfLongestSubstring(s))

# Output: 3
# Explanation: The answer is "abc", with the length of 3.