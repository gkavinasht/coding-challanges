# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

def searchRange(nums, target):
    def binarySearchLeft(nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def binarySearchRight(nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return r

    left_index = binarySearchLeft(nums, target)
    right_index = binarySearchRight(nums, target)

    if left_index <= right_index:
        return [left_index, right_index]
    else:
        return [-1, -1]

nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target))

# Time Complexity: O(logn)
# Space Complexity: O(1)
# Output: [3,4]