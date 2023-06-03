# 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

def sortedSquares(nums):
    res = []
    l = 0
    r = len(nums) - 1
    while l <= r:
        left = abs(nums[l])
        right = abs(nums[r])

        if left > right:
            res.append(left*left)
            l += 1
        else:
            res.append(right*right)
            r -= 1
    return res[::-1]

    # Time Complexity: O(n)
    # Space Complexity: O(1)

    # res = []
    # for n in nums:
    #     res.append(n*n)
    # res.sort()
    # return res

    # Time Complexity: O(n)
    # Space Complexity: O(1)

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))

# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Time Complexity: O(n)
# Space Complexity: O(1)