# 98. Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: TreeNode) -> bool:
	def validate(root, low=float('-inf'), high=float('inf')):
		if root is None:
			return True
		if root.val <= low or root.val >= high:
			return False
		return validate(root.left, low, root.val) and validate(root.right, root.val, high)

	return validate(root)

# root = [2,1,3]
first_node = TreeNode(2)
second_node = TreeNode(1)
third_node = TreeNode(3)

first_node.left = second_node
first_node.right = third_node
root = first_node
print(isValidBST(root))

# Output: true