# 257. Binary Tree Paths
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def allPathsToLeaf(root):
    def dfs(node, path, result):
        if not node:
            return

        path.append(node.val)

        if not node.left and not node.right:
            result.append("->".join(map(str, path)))

        dfs(node.left, path, result)
        dfs(node.right, path, result)

        path.pop()

    result = []
    dfs(root, [], result)
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

paths = allPathsToLeaf(root)
print(paths)

# Time Complexity: O(n)
# Space Complexity: O(n)