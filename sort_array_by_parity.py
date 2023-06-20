# 905. Sort Array By Parity
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.

def sortArrayByParity(nums):
    i, j = 0, 0
    while j < len(nums):
        if nums[j] % 2 == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    return nums

nums = [3,1,2,4]
print(sortArrayByParity(nums))

# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Time Complexity: O(n)
# Space Complexity: O(1)