# 104. Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode):
    # Recursion
    if root is None:
        return 0
    
    left_ans = maxDepth(root.left)
    right_ans = maxDepth(root.right)
    
    return 1 + max(left_ans, right_ans)

    # Iteration
    # if not root:
    #     return 0

    # queue = collections.deque()
    # queue.append((root, 1))

    # while queue:
    #     node, depth = queue.popleft()

    #     if node.left:
    #         queue.append((node.left, depth + 1))

    #     if node.right:
    #         queue.append((node.right, depth + 1))

    # return depth

# Time complexity: O(n)
# Space Complexity: O(n)

# root = [3,9,20,null,null,15,7]
node_1 = TreeNode(3)
node_2 = TreeNode(9)
node_3 = TreeNode(20)
node_4 = TreeNode(15)
node_5 = TreeNode(7)

node_1.left = node_2
node_1.right = node_3
node_3.left = node_4
node_3.right = node_5
root = node_1

print(maxDepth(root))
# Output: 3