# 652. Find Duplicate Subtrees
# Given the root of a binary tree, return all duplicate subtrees.
# For each kind of duplicate subtrees, you only need to return the root node of any one of them.
# Two trees are duplicate if they have the same structure with the same node values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findDuplicateSubtrees(root: TreeNode):
    def traverse(node):
        if not node:
            return ""

        serial = f"{node.val},{traverse(node.left)},{traverse(node.right)}"
        mydict[serial] = mydict.get(serial, 0) + 1
        if mydict[serial] == 2:
            res.append(node)
        return serial
    mydict = {}
    res = []
    traverse(root)
    return res

# root = [1,2,3,4,null,2,4,null,null,4]

# Create the tree nodes
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4_1 = TreeNode(4)
node4_2 = TreeNode(4)
node2_1 = TreeNode(2)
node4_3 = TreeNode(4)
node4_4 = TreeNode(4)

# Connect the nodes to form the tree
node1.left = node2
node1.right = node3
node2.left = node4_1
node2.right = None
node3.left = node2_1
node3.right = node4_2
node2_1.left = node4_3
node2_1.right = None
node4_2.left = None
node4_2.right = node4_4

# Set the root of the tree
root = node1

res_node = findDuplicateSubtrees(root)
for node in res_node:
    print(node.val)
    if node.left:
        print(node.left.val)
    if node.right:
        print(node.right.val)

# Time Complexity: O(n)
# Space Complexity: O(n)

# Output: [[2,4],[4]]