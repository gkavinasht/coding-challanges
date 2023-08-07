# 101. Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode):
    def isMirror(tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None or tree2 is None:
            return False
        if tree1.val != tree2.val:
            return False
        return isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left)
    
    return isMirror(root, root)

# root = [1,2,2,3,4,4,3]
node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(2)
node_6 = TreeNode(4)
node_7 = TreeNode(3)

node_1.left = node_2
node_1.right = node_5
node_2.left = node_3
node_2.right = node_4
node_5.left = node_6
node_5.right = node_7
root = node_1

print(isSymmetric(root))

# Time Complexity: O(n)
# Space Complexity: O(n)

# Output: true