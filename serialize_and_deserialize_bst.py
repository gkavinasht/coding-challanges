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
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(str(root.val))
                inorder(root.right)

            return res

        inorder(root)
        return ' '.join(res)

    def deserialize(self, data):
        def constructTree(data):
            if not data:
                return None
                
            ind = len(data) // 2
            root = TreeNode(data[ind])
            root.left = constructTree(data[:ind])
            root.right = constructTree(data[ind + 1:])

            return root
            
        data = [int(x) for x in data.split(' ') if x]
        return constructTree(data)

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