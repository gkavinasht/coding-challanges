# 450. Delete Node in a BST
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
# Basically, the deletion can be divided into two stages:
# Search for a node to remove.
# If the node is found, delete the node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def predecessor(root):
	root = root.left
	while root.right:
		root = root.right
	return root.val

def successor(root):
	root = root.right
	while root.left:
		root = root.left
	return root.val

def deleteNode(root, key):
	if root is None:
		return None

	if root.val > key:
		root.left = deleteNode(root.left, key)
	elif root.val < key:
		root.right = deleteNode(root.right, key)
	else:
		# If root has no child or one child
		if not (root.left or root.right):
			root = None
		elif root.right:
			# Replace the current root val with the successor val (lowest ele in right sub tree)
			root.val = successor(root)
			# Delete the successor val from right sub tree as the current root val is replaced with successor val
			root.right = deleteNode(root.right, root.val)
		else:
			# Replace the current root val with the predecessor val (highest ele in left sub tree)
			root.val = predecessor(root)
			# Delete the predecessor val from left sub tree as the current root val is replaced with predecessor val
			root.left = deleteNode(root.left, root.val)

# root = [5,3,6,2,4,null,7]
key = 3

node_1 = TreeNode(5)
node_2 = TreeNode(3)
node_3 = TreeNode(6)
node_4 = TreeNode(2)
node_5 = TreeNode(4)
node_6 = TreeNode(7)

node_1.left = node_2
node_1.right = node_3
node_2.left = node_4
node_2.right = node_5
node_3.right = node_6
root = node_1

res_node = deleteNode(root, key)
print(res_node.left.val)

# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Time Complexity: O(n)
# Space Complexity: O(n)