# 701. Insert into a Binary Search Tree
# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
	# Iteration
    if root is None:
        return TreeNode(val)

    prev = None
    curr = root

    while curr:
        prev = curr
        if val < curr.val:
            curr = curr.left
        else:
            curr = curr.right

    if val < prev.val:
        prev.left = TreeNode(val)
    else:
        prev.right = TreeNode(val)

    return root

    # Time Complexity: O(n)
	# Space Complexity: O(1)

	# Recursion
	# if root is None:
	# 	return TreeNode(val)

	# if root.val == val:
	# 	return root
	# elif root.val > val:
	# 	root.left = insertIntoBST(root.left, val)
	# elif root.val < val:
	# 	root.right = insertIntoBST(root.right, val)
	# return root

	# Time Complexity: O(h)
	# Space Complexity: O(h)

# root = [4,2,7,1,3]
val = 5

node_1 = TreeNode(4)
node_2 = TreeNode(2)
node_3 = TreeNode(7)
node_4 = TreeNode(1)
node_5 = TreeNode(3)

node_1.left = node_2
node_1.right = node_3
node_2.left = node_4
node_3.right = node_5
root = node_1

res_node = insertIntoBST(root, val)
print(res_node.right.left.val)

# Output: [4,2,7,1,3,5]

# Time Complexity: O(h)
# Space Complexity: O(h)