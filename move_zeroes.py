# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i, j = 0, 0
    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)

# Output: [1,3,12,0,0]

# Time Complexity: O(n)
# Space Complexity: O(1)