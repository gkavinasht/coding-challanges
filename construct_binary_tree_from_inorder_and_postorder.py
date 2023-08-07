# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None

    # Last element in postorder is the root element
    ele = postorder.pop()
    root = TreeNode(ele)
    i = inorder.index(ele)

    # Construct right tree first as postorder.pop() gives right element first
    root.right = buildTree(inorder[i + 1:], postorder)
    root.left = buildTree(inorder[:i], postorder)

    return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
res_node = buildTree(inorder, postorder)
print(res_node.val)

# Time Complexity: O(n)
# Space Complexity: O(n)

# Output: [3,9,20,null,null,15,7]