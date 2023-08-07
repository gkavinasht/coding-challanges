# 112. Path Sum
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum. A leaf is a node with no children.

import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum):
    # Recursion
    # if not root:
    #     return False

    # targetSum -= root.val

    # if not root.left and not root.right and targetSum == 0:
    #     return True

    # return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

    # Iteration
    queue = collections.deque()
    queue.append((root, targetSum))

    while queue:
        curr, currSum = queue.popleft()

        if curr:
            if not curr.left and not curr.right and currSum == curr.val:
                return True

            queue.append((curr.left, currSum - curr.val))
            queue.append((curr.right, currSum - curr.val))
    return False

# Time Complexity: O(n)
# Space Complexity: O(n)

# root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
node_1 = TreeNode(5)
node_2 = TreeNode(4)
node_3 = TreeNode(8)
node_4 = TreeNode(11)
node_5 = TreeNode(13)
node_6 = TreeNode(4)
node_7 = TreeNode(7)
node_8 = TreeNode(2)
node_9 = TreeNode(1)

node_1.left = node_2
node_1.right = node_3
node_2.left = node_4
node_4.left = node_7
node_4.right = node_8
node_3.left = node_5
node_3.right = node_6
node_6.right = node_9
root = node_1
targetSum = 22

print(hasPathSum(root, targetSum))

# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.