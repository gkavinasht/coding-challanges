# 394. Decode String
# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
# The test cases are generated so that the length of the output will never exceed 105.

def decodeString(s):
	stack = []
    currNum = 0
    currStr = ''

    for c in s:
        if c == '[':
            stack.append(currStr)
            stack.append(currNum)
            currStr = ''
            currNum = 0
        elif c == ']':
            num = stack.pop()
            prevStr = stack.pop()
            currStr = prevStr + num * currStr
        elif c.isdigit(): # curNum*10+int(c) is helpful in keep track of more than 1 digit number
            currNum = currNum*10 + int(c)
        else:
            currStr += c
    return currStr
        
    # left = 0
    # stack = [""]
    # num_stack = []

    # while left < len(s):
    #     if s[left].isdigit():
    #         digit = ""
    #         # Convert the string to int as it can double digits
    #         while s[left].isdigit():
    #             digit += s[left]
    #             left += 1

    #         digit_int = int(digit)
    #         stack.append("")
    #         num_stack.append(digit_int)

    #     elif s[left] == ']':
    #         mul_string = num_stack.pop()
    #         top_str = stack.pop()
    #         stack[-1] += mul_string * top_str
    #     else:
    #         stack[-1] += s[left]
    #     left += 1

    # return stack[0]

s = "3[a]2[bc]"
print(decodeString(s))

# Time Complexity: O(n)
# Space Complexity: O(n)

# Output: "aaabcbc"