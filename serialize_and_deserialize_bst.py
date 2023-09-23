#!/usr/bin/python
# -*- coding: utf-8 -*-

# 449. Serialize and Deserialize BST
# Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.
# The encoded string should be as compact as possible.

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """
    ....Encodes a tree to a single string.
        """
        output = []
        def postorder(root):
            if root is None:
                return []
            
            postorder(root.left)
            postorder(root.right)
            output.append(str(root.val))
            
            return output
        return ' '.join(postorder(root))

    def deserialize(self, data):
        def helper(lower = float('-inf'), upper = float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None
            
            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root
        
        data = [int(x) for x in data.split(' ') if x]
        return helper()

# root = [2,1,3]

first_node = TreeNode(2)
second_node = TreeNode(1)
third_node = TreeNode(3)

first_node.left = second_node
first_node.right = third_node
root = first_node

ser = Codec()
deser = Codec()
tree = ser.serialize(root)
print(tree)
ans = deser.deserialize(tree)
print(ans.val)
print(ans.left.val)
print(ans.right.val)

# Output: [2,1,3]

# Time Complexity: O(n)
# Space Complexity: O(n)