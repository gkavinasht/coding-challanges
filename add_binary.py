# 67. Add Binary
# Given two binary strings a and b, return their sum as a binary string.

def addBinary(a, b):
    res = ""
    carry = 0

    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        digit_sum = digit_a + digit_b + carry
        carry = digit_sum // 2
        digit_sum %= 2

        res = str(digit_sum) + res
        i -= 1
        j -= 1

    return res

a = "11"
b = "1"
print(addBinary(a, b))

# Output: "100"

# Time Complexity: O(n)
# Space Complexity: O(1)