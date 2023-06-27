# 561. Array Partition
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

def arrayPairSum(nums):
	# Time Complexity: O(n)
    # Space Complexity: O(1)

    # nums.sort()
    # max_sum = 0
    # for i in range(0, len(nums), 2):
    #     max_sum += nums[i]
    # return max_sum

    # Time Complexity: O(nlogn) --> Built-in sort()
    # Space Complexity: O(n) --> Built-in sort()

nums = [1,4,3,2]
print(arrayPairSum(nums))

# Output: 4
# Explanation: All possible pairings (ignoring the ordering of elements) are:
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# So the maximum possible sum is 4.