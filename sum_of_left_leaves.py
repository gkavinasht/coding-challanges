# 404. Sum of Left Leaves
# Given the root of a binary tree, return the sum of all left leaves.
# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root):
    res = 0
    queue = collections.deque([root])

    while queue:
        curr = queue.popleft()

        if curr.left:
            queue.append(curr.left)
            if not curr.left.left and not curr.left.right:
                res += curr.left.val
        if curr.right:
            queue.append(curr.right)
    return res

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

print(sumOfLeftLeaves(root))

# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.