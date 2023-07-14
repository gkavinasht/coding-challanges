# 75. Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    curr, p1, p2 = 0, 0, len(nums) - 1
    while curr <= p2:
        if nums[curr] == 0:
            nums[p1], nums[curr] = nums[curr], nums[p1]
            p1 += 1
            curr += 1
        elif nums[curr] == 2:
            nums[curr], nums[p2] = nums[p2], nums[curr]
            p2 -= 1
        else:
            curr += 1

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)

# Time Complexity: O(n)
# Space Complexity: O(1)

# Output: [0,0,1,1,2,2]