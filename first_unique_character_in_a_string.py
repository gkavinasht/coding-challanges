# 387. First Unique Character in a String
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

def firstUniqChar(s):
    mydict = {}
    for i in range(len(s)):
        mydict[s[i]] = mydict.get(s[i], 0) + 1

    for i in range(len(s)):
        if mydict[s[i]] == 1:
            return i
    return -1

s = "leetcode"
print(firstUniqChar(s))

# Output: 0First Unique Character in a String