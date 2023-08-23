# 285. Inorder Successor in BST

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderSuccessor(root, p):
	successor = None

	while root:
		if p.val < root.val:
			successor = root
			root = root.left
		else:
			root = root.right

	return successor

# root = [2,1,3]
first_node = TreeNode(2)
second_node = TreeNode(1)
third_node = TreeNode(3)

first_node.left = second_node
first_node.right = third_node
root = first_node
res = inorderSuccessor(root, first_node)
print(res.val)

# Output: 3

# Time Complexity: O(n)
# Space Complexity: O(1)