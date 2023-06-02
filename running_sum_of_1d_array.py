# 1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.

def runningSum(nums):
    res = [0] * len(nums)
    res[0] = nums[0]
    for i in range(1, len(nums)):
        res[i] = res[i-1] + nums[i]
    return res

nums = [1,2,3,4]
print(runningSum(nums))

# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Time Complexity : O(n)
# Space Complexity : O(1)