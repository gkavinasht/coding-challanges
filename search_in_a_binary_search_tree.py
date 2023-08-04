# 700. Search in a Binary Search Tree
# You are given the root of a binary search tree (BST) and an integer val. Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root: TreeNode, val: int):
    # Recursion
    # if root is None:
    #     return None

    # if root.val == val:
    #     return root

    # return self.searchBST(root.left, val) or self.searchBST(root.right, val)

    # Time Complexity: O(n)
	# Space Complexity: O(n)

    # Iteration
    if not root:
        return None
        
    queue = collections.deque()
    queue.append(root)

    while queue:
        node = queue.popleft()

        if node.val == val:
            return node

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return None

    # Time Complexity: O(n)
	# Space Complexity: O(n)

# root = [4,2,7,1,3]
val = 2

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

res_node = searchBST(root, val)
print(res_node.val)
# Output: [2,1,3]