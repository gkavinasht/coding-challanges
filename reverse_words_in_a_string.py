# 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. 
# The returned string should only have a single space separating the words. Do not include any extra spaces.

def reverseWords(s):
	# Stack
    s = s + " "
    stack = []
    word = ""

    i = 0
    while i < len(s):
        if s[i] == " ":
            stack.append(word)
            word = ""
        elif s[i] != " ":
            word += s[i]
        i += 1

    res = ""
    while stack:
        eachWord = stack.pop()
        if eachWord:
            res += eachWord + " "
    return res.strip()

    # words = s.strip().split(" ")
    # res = ""
    # for i in range(len(words)-1, -1, -1):
    #     if words[i]:
    #         res += words[i] + " "
    # return res.strip()

s = "the sky is blue"
print(reverseWords(s))

# Time Complexity: O(n)
# Space Complexity: O(n)

# Output: "blue is sky the"