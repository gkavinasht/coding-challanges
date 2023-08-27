# 110. Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    def height(root):
        if root is None:
            return 0

        leftHeight, rightHeight = height(root.left), height(root.right)
        if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) > 1:
            return -1
        
        return max(leftHeight, rightHeight) + 1
    
    return height(root) >= 0

# root = [3,9,20,null,null,15,7]

first_node = TreeNode(3)
second_node = TreeNode(9)
third_node = TreeNode(20)
fourth_node = TreeNode(15)
fifth_node = TreeNode(7)

first_node.left = second_node
first_node.right = third_node
third_node.left = fourth_node
third_node.right = fifth_node
root = first_node

print(isBalanced(root))

# Output: true

# Time Complexity: O(n)
# Space Complexity: O(n)