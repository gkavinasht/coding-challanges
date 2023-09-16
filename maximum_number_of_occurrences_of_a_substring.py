# 1297. Maximum Number of Occurrences of a Substring
# Given a string s, return the maximum number of occurrences of any substring under the following rules:
# The number of unique characters in the substring must be less than or equal to maxLetters.
# The substring size must be between minSize and maxSize inclusive.

def maxFreq(s, maxLetters, minSize, maxSize):
    validSubs = {}
    for i in range(len(s)):
        currStr = s[i]
        currCount = 1
        if currCount <= maxLetters and len(currStr) >= minSize and len(currStr) <= maxSize:
            validSubs[currStr] = validSubs.get(currStr, 0) + 1
        for j in range(i + 1, len(s)):
            if s[j] not in currStr:
                currCount += 1
            currStr += s[j]
            
            if len(currStr) > maxSize:
                break
            if currCount <= maxLetters and len(currStr) >= minSize and len(currStr) <= maxSize:
                validSubs[currStr] = validSubs.get(currStr, 0) + 1

    if validSubs:
        validSubsList = sorted(validSubs.items(), key = lambda x: -x[1])
        return validSubsList[0][1]
    return 0

s = "aababcaab"
maxLetters = 2
minSize = 3
maxSize = 4
print(maxFreq(s, maxLetters, minSize, maxSize))

# Output: 2
# Explanation: Substring "aab" has 2 occurrences in the original string.
# It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

# Time complexity: O(n**2)
# Space Complexity: O(n)