# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums, target):
    numsdict = {}
    for i in range(len(nums)):
        rem = target - nums[i]
        if rem in numsdict:
            return [numsdict[rem], i]
        numsdict[nums[i]] = i
    return []

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))

# Time Complexity: O(n)
# Space Complexity: O(n)

# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].