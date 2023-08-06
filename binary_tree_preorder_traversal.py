# 144. Binary Tree Preorder Traversal
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root: TreeNode):
    # Recursion
    # def preOrder(root, res):
    #     if not root:
    #         return None

    #     # Visit root first, then the left subtree, then the right subtree.
    #     res.append(root.val)
    #     preOrder(root.left, res)
    #     preOrder(root.right, res)

    #     return res
        
    # res = []
    # return preOrder(root, res)

    # Time Complexity: O(n)
    # Space Complexity: O(n)

    # Iteration
    res = []
    stack = []
    stack.append(root)

    # Note that we add curr_node's right child to the stack first (LIFO)
    while stack:
        currNode = stack.pop()

        if currNode:
            res.append(currNode.val)
            stack.append(currNode.right)
            stack.append(currNode.left)

    return res

    # Time Complexity: O(n)
    # Space Complexity: O(n)

# root = [1,null,2,3]
node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)

node_1.right = node_2
node_2.left = node_3
root = node_1

print(preorderTraversal(root))
# Output: [1,2,3]