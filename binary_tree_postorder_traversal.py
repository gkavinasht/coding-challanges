# 145. Binary Tree Postorder Traversal
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    # Recursion
    # def postOrder(root, res):
    #     if not root:
    #         return None

    #     if root.left:
    #         postOrder(root.left, res)
    #     if root.right:
    #         postOrder(root.right, res)
    #     res.append(root.val)

    # res = []
    # postOrder(root, res)
    # return res

    # Iteration-1
    res = []
    stack = []
    prev = None
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack[-1]

        if not curr.right or curr.right == prev:
            res.append(curr.val)
            stack.pop()
            prev = curr
            curr = None
        else:
            curr = curr.right

    return res

    # Iteration-2
    # res = []
    # stack = []
    # stack.append(root)

    # while stack:
    #     curr = stack.pop()

    #     if curr:
    #         res.append(curr.val)
    #         stack.append(curr.left)
    #         stack.append(curr.right)

    # return res[::-1]

# root = [1,null,2,3]

node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)

node_1.right = node_2
node_2.left = node_3
root = node_1

print(postorderTraversal(root))

# Time Complexity : O(n)
# Space Complexity : O(n)

# Output: [3,2,1]