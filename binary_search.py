# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

def binary_search(nums, target):
    if len(nums) == 0:
        return -1

    l = 0
    r = len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
    return -1

nums = [-1,0,3,5,9,12]
target = 9

print(binary_search(nums, target))

# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Time Complexity : O(logn)
# Space Complexity: O(1)