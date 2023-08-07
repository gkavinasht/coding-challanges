# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    ele = preorder.pop(0)
    root = TreeNode(ele)
    index = inorder.index(ele)

    root.left = buildTree(preorder, inorder[:index])
    root.right = buildTree(preorder, inorder[index + 1:])

    return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
res_node = buildTree(preorder, inorder)
print(res_node.val)

# Time Complexity: O(n)
# Space Complexity: O(n)

# Output: [3,9,20,null,null,15,7]