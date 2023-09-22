# 199. Binary Tree Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    levels = collections.defaultdict(list)
    if not root:
        return []

    queue = collections.deque([(root, 0)])
    while queue:
        curr_node, curr_level = queue.popleft()
        if curr_level in levels:
            levels[curr_level].append(curr_node.val)
        else:
            levels[curr_level] = [curr_node.val]

        if curr_node.left:
            queue.append((curr_node.left, curr_level + 1))

        if curr_node.right:
            queue.append((curr_node.right, curr_level + 1))

    return [nodes[-1] for _, nodes in levels.items()]

# root = [1,2,3,null,5,null,4]
first_node = TreeNode(1)
second_node = TreeNode(2)
third_node = TreeNode(3)
fourth_node = TreeNode(4)
fifth_node = TreeNode(5)

first_node.left = second_node
first_node.right = third_node
second_node.right = fifth_node
third_node.right = fourth_node

root = first_node
print(rightSideView(root))

# Output: [1,3,4]

# Time Complexity: O(n)
# Space Complexity: O(n)