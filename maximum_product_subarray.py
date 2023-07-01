# 152. Maximum Product Subarray
# Given an integer array nums, find a subarray that has the largest product, and return the product.

def maxProduct(nums):
	# Dynamic Programming
    if not nums:
        return 0

    max_so_far, min_so_far, max_product = nums[0], nums[0], nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_so_far, min_so_far = min_so_far, max_so_far

        max_so_far = max(nums[i], max_so_far * nums[i])
        min_so_far = min(nums[i], min_so_far * nums[i])

        max_product = max(max_product, max_so_far)

    return max_product

nums = [2,3,-2,4]
print(maxProduct(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Output: 6
# Explanation: [2,3] has the largest product 6.