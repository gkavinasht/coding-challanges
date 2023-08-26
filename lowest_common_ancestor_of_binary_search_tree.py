# 235. Lowest Common Ancestor of a Binary Search Tree
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
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

    while q not in ancestors:
        q = parent[q]

    return q

# root = [6,2,8,0,4,7,9,null,null,3,5]
# p = 2
# q = 8

first_node = TreeNode(6)
second_node = TreeNode(2)
third_node = TreeNode(8)
fourth_node = TreeNode(0)
fifth_node = TreeNode(4)
sixth_node = TreeNode(7)
seventh_node = TreeNode(9)
eighth_node = TreeNode(3)
ninth_node = TreeNode(5)

first_node.left = second_node
first_node.right = third_node
second_node.left = fourth_node
second_node.right = fifth_node
fifth_node.left = eighth_node
fifth_node.right = ninth_node
third_node.left = sixth_node
third_node.right = seventh_node

root = first_node
res_node = lowestCommonAncestor(root, second_node, third_node)
print(res_node.val)

# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Time Complexity: O(n)
# Space Complexity: O(n)