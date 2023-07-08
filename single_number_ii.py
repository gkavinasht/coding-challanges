# 137. Single Number II
# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber(nums):
    ones = 0 # To track number occuring once
    twos = 0 # To track number occuring twice

    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones

    return ones

# Time Complexity: O(n)
# Space Complexity: O(1)

nums = [2, 2, 3, 2]
print(singleNumber(nums))

# Output: 3