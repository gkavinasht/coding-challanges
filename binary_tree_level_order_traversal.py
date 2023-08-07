# 102. Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode):
    res = []
    if not root:
        return res

    queue = collections.deque()
    queue.append((root, 1))

    while queue:
        curr, level = queue.popleft()

        if level > len(res):
            res.append([curr.val])
        else:
            res[level - 1].append(curr.val)

        if curr.left:
            queue.append((curr.left, level + 1))
        if curr.right:
            queue.append((curr.right, level + 1))

    return res

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

print(levelOrder(root))

# Output: [[3],[9,20],[15,7]]
