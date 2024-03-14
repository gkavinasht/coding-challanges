"""
1698. Number of Distinct substrings in a string
Given a string s, return the number of distinct substrings of s.

A substring of a string is obtained by deleting any number of characters (possibly zero) from the front of the string and any number (possibly zero) from the back of the string.

Example 1:

Input: s = "aabbaba"
Output: 21
Explanation: The set of distinct strings is ["a","b","aa","bb","ab","ba","aab","abb","bab","bba","aba","aabb","abba","bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]
Example 2:

Input: s = "abcdefg"
Output: 28
"""

def countDistinct(self, s: str) -> int:
    trie = {}
    res = 0

    for i in range(len(s)):
        node = trie
        for j in range(i, len(s)):
            if s[j] not in node:
                node[s[j]] = {'end': True}

            node = node[s[j]]

            if node['end'] == True:
                node['end'] = False
                res += 1

    return res

    # res = set()

    # for i in range(len(s)):
    #     for j in range(i, len(s)):
    #         if s[i:j + 1] not in res:
    #             res.add(s[i:j + 1])

    # return len(res)