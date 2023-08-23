# 236. Lowest Common Ancestor of a Binary Tree
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
	parent = {}
	parent[root] = None

	stack = collections.deque([root])

	while p not in parent or q not in parent:
		curr = stack.popleft()

		if curr.left:
			parent[curr.left] = curr
			stack.append(curr.left)

		if curr.right:
			parent[curr.right] = curr
			stack.append(curr.right)

	ancestors = set()
	while p:
		ancestors.add(p)
		p = parent[p]

	while q and q not in ancestors:
		q = parent[q]

	return q

# root = [3,5,1,6,2,0,8,null,null,7,4]
# p = 5
# q = 1
first_node = TreeNode(3)
second_node = TreeNode(5)
third_node = TreeNode(1)
fourth_node = TreeNode(6)
fifth_node = TreeNode(2)
sixth_node = TreeNode(0)
seventh_node = TreeNode(8)
eighth_node = TreeNode(7)
ninth_node = TreeNode(4)

first_node.left = second_node
first_node.right = third_node
second_node.left = fourth_node
second_node.right = fifth_node
fifth_node.left = eighth_node
fifth_node.right = ninth_node
third_node.left = sixth_node
third_node.right = seventh_node

root = first_node
p = second_node
q = third_node
res = lowestCommonAncestor(root, p, q)
print(res.val)

# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Time Complexity: O(n)
# Space Complexity: O(n)