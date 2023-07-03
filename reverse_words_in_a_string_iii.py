# 557. Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

def reverseWords(s):
    res = ""
    word = []
    s = s + " "
    for i in range(len(s)):
        if s[i] != " ":
            word.append(s[i])
        elif s[i] == " ":
            while word:
                res += word.pop()
            res += s[i]
            word = []
        i += 1
    return res.strip()

s = "Let's take LeetCode contest"
print(reverseWords(s))

# Output: "s'teL ekat edoCteeL tsetnoc"