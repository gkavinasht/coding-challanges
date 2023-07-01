# 713. Subarray Product Less Than K
# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0

    left, right, res, curr = 0, 0, 0, 1

    while right < len(nums):
        curr *= nums[right]
        
        while curr >= k:
            curr //= nums[left]
            left += 1

        res += right - left + 1
        right += 1
    return res

nums = [10,5,2,6]
k = 100
print(numSubarrayProductLessThanK(nums, k))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.