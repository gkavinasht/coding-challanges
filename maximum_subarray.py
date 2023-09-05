# 53. Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

def maxSubArray(nums):
    if len(nums) == 0:
        return 0

    globalMax, currMax = nums[0], nums[0]

    for i in range(1, len(nums)):
        currMax = max(nums[i], currMax + nums[i])

        if currMax > globalMax:
            globalMax = currMax

    return globalMax

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))

# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Time Complexity: O(n)
# Space Complexity: O(n)