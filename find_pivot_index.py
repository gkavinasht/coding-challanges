# 724. Find Pivot Index
# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

def pivotIndex(nums):
    total_sum = sum(nums)
    current_sum = 0
    for i in range(len(nums)):
        if current_sum == total_sum - current_sum - nums[i]:
            return i
        current_sum += nums[i]
    return -1

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11