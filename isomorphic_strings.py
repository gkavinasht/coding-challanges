# 205. Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

def isIsomorphic(s, t):
    if len(set(s)) != len(set(t)):
        return False

    mydict = {}
    for i in range(len(s)):
        if s[i] not in mydict:
            mydict[s[i]] = t[i]
        elif mydict[s[i]] != t[i]:
            return False
    return True

    # # Dictionary with keys as chars of s and values as chars of t
    # mydict = {}
    # # To store unique/visited characters of t
    # val = ""
    # for i in range(len(s)):
    #     if s[i] not in mydict:
    #         # t[i] has to be new and not present in val
    #         if t[i] not in val:
    #             mydict[s[i]] = t[i]
    #             val += t[i]
    #         else:
    #             return False
    #     else:
    #         if mydict[s[i]] != t[i]:
    #             return False
    # return True

s = "egg"
t = "add"
print(isIsomorphic(s, t))

# Time Complexity: O(n)
# Space Complexity: O(n)

# Output: true