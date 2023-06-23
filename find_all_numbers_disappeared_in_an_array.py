# 448. Find All Numbers Disappeared in an Array
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

def findDisappearedNumbers(nums):
    res = []
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = -abs(nums[index])

    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i + 1)
    return res

    # Time Complexity: O(n)
    # Space Complexity: O(1)

    # nums_set = set(nums)
    # length = len(nums)
    # res = []
    # for i in range(1, length + 1):
    #     if i not in nums_set:
    #         res.append(i)
    # return res

    # Time Complexity: O(n)
    # Space Complexity: O(n)

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))

# Output: [5,6]