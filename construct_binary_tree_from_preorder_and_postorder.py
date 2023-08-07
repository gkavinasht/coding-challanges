# 889. Construct Binary Tree from Preorder and Postorder Traversal
# Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree. If there exist multiple answers, you can return any of them.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructFromPrePost(pre, post):
    if not pre or not post:
        return None

    root = TreeNode(pre[0])
    if len(pre) == 1:
        return root

    left_size = post.index(pre[1]) + 1

    root.left = constructFromPrePost(pre[1:left_size + 1], post[:left_size])
    root.right = constructFromPrePost(pre[left_size + 1:], post[left_size:])

    return root

preorder = [1,2,4,5,3,6,7]
postorder = [4,5,2,6,7,3,1]

res_node = constructFromPrePost(preorder, postorder)
print(res_node.val)

# Time Complexity: O(n)
# Space Complexity: O(n)

# Output: [1,2,3,4,5,6,7]