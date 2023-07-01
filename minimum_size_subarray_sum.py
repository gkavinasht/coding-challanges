# 209. Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

import math

def minSubArrayLen(target, nums):
	# Sliding Window Approach
    left, right, currentSum = 0, 0, 0
    min_length = math.inf

    while right < len(nums):
        currentSum += nums[right]

        while currentSum >= target:
            min_length = min(min_length, right - left + 1)
            currentSum -= nums[left]
            left += 1
        right += 1

    return min_length if min_length != math.inf else 0

    # Time Complexity: O(n)
    # Space Complexity: O(1)

    # if target in nums:
    #     return 1

    # min_length = math.inf
    # for i in range(len(nums)):
    #     for j in range(i, len(nums)):
    #         subarray = nums[i:j+1]
    #         if not any(subarray) > target:
    #             if sum(subarray) >= target:
    #                 min_length = min(len(subarray), min_length)
    # return min_length if min_length != math.inf else 0

    # Time Complexity: O(n*2)
    # Space Complexity: O(1)

target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))

# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.