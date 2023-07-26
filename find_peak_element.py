# 162. Find Peak Element
# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
# You must write an algorithm that runs in O(log n) time.

def findPeakElement(nums):
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            if i == len(nums) - 1:
                return i
            if nums[i] > nums[i + 1]:
                return i
    return 0

nums = [1,2,3,1]
print(findPeakElement(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.