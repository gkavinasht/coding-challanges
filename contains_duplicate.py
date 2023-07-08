# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums):
    numSet = set()
    for num in nums:
        if num in numSet:
            return True
        numSet.add(num)
    return False

nums = [1,2,3,1]
print(containsDuplicate(nums))

# Time Complexity: O(n)
# Space Complexity: O(n)
# Output: true