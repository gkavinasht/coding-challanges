# 94. Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def helper(self, root, res):
    #     if not root:
    #         return None

    #     self.helper(root.left, res)
    #     res.append(root.val)
    #     self.helper(root.right, res)

    #     return res

    def inorderTraversal(self, root):
        # Using Recursion
        # return self.helper(root, [])

        # Using Stack
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

# root = [1,null,2,3]

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

s = Solution()
print(s.inorderTraversal(root))

# Both Recursion and Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

# Output: [1,3,2]