# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def getKey(s):
	return str(sorted(s))

# Time Complexity: O(m * nlogn) -> Built-in sort
# Space Complexity: O(m * n) -> Built-in sort

# def getkey(s):
#     add = 0
#     mul = 1
#     for char in s:
#         add += ord(char)
#         mul *= ord(char)
#     return add*mul

# Time Complexity: O(m * n)
# Space Complexity: O(n)

def groupAnagrams(strs):
    strsdict = {}
    res = []

    for s in strs:
        key = getKey(s)
        if key in strsdict:
            val = strsdict[key]
            val.append(s)
        else:
            strsdict[key] = [s]

    return strsdict.values()

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]