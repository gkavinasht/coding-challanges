# 108. Convert Sorted Array to Binary Search Tree
# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced binary search tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    def helper(left, right):
        if left <= right:
            p = (left + right) // 2
            
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            
            return root
    return helper(0, len(nums) - 1)

nums = [-10,-3,0,5,9]
res_node = sortedArrayToBST(nums)
print(res_node.val)

# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Time Complexity: O(n)
# Space Complexity: O(logn) -> max call stack depth