# 66. Plus One
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

def plusOne(digits):
    n = len(digits)
    carry = 0

    for i in range(n - 1, -1, -1):
        if i == n - 1:
            increment_digit = digits[i] + 1
        else:
            increment_digit = digits[i] + carry
            carry = 0
        digits[i] = increment_digit % 10
        carry = increment_digit // 10

    if carry == 1:
        return [1] + digits
    return digits

digits = [1,2,3]
print(plusOne(digits))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].