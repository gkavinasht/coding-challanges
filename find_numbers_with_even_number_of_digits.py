# 1295. Find Numbers with Even Number of Digits
# Given an array nums of integers, return how many of them contain an even number of digits.

def findNumbers(nums):
    evenDigitNumbers = 0
    for n in nums:
        numberLength = 0
        while n > 0:
            numberLength += 1
            n = n // 10
        if numberLength % 2 == 0:
            evenDigitNumbers += 1
    return evenDigitNumbers

nums = [12,345,2,6,7896]
print(findNumbers(nums))

# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.

# Time Complexity : O()
# Space Complexity : O()