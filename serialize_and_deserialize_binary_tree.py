# 297. Serialize and Deserialize Binary Tree
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, string):
        	if root is None:
        		string += "None "
        	else:
        		string += str(root.val) + " "
        		string = rserialize(root.left, string)
        		string = rserialize(root.right, string)

        	return string
        return rserialize(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(d):
        	if d[0] == "None":
        		d.pop(0)
        		return None

	        x = d.pop(0)
	        root = TreeNode(x)

	        root.left = rdeserialize(d)
	        root.right = rdeserialize(d)

	        return root

        d = data.strip().split(' ')
        return rdeserialize(d)


# root = [1,2,3,null,null,4,5]
first_node = TreeNode(1)
second_node = TreeNode(2)
third_node = TreeNode(3)
fourth_node = TreeNode(4)
fifth_node = TreeNode(5)

first_node.left = second_node
first_node.right = third_node
third_node.left = fourth_node
third_node.right = fifth_node
root = first_node

ser = Codec()
deser = Codec()
tree_str = ser.serialize(root)
ans = deser.deserialize(tree_str)
print(ans.val)

# Output: [1,2,3,null,null,4,5]

# Time Complexity: O(n)
# Space Complexity: O(n)