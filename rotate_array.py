# 189. Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)

    # Time Complexity : O(n)
    # Space Complexity : O(1)

    # length = len(nums)
    # while k > 0:
    #     tmp = nums[length - 1]
    #     for i in range(length - 1, 0, -1):
    #         nums[i] = nums[i - 1]
    #     nums[0] = tmp
    #     k -= 1

    # Time Complexity : O(kn)
    # Space Complexity : O(1)

nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums, k)
print(nums)

# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]