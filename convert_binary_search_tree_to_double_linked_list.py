# 426. Convert Binary Search Tree to Double Linked List
# Write a code to convert a given binary tree to a Doubly Linked List (DLL) in place. 
# The left and right pointers in the nodes are to be used as previous and next pointers, respectively, in the converted DLL.

class ListNode:
	def __init__(self, val):
		self.val = val
		self.prev = None
		self.next = None

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class ConvertTreeLinkedList:
	def printList(self, head):
		curr = head
		while curr:
			print(curr.val)
			curr = curr.next

	def convert_tree_to_linked_list(self, root):
		if not root:
			return None

		head = None
		prev = None
		current = root
		queue = []

		while current or queue:
			while current:
				queue.append(current)
				current = current.left

			current = queue.pop()

			dll_node = ListNode(current.val)

			if prev:
				prev.next = dll_node
				dll_node.prev = prev
			else:
				head = dll_node
			prev = dll_node

			current = current.right

		return head

first_node = TreeNode(4)
second_node = TreeNode(3)
third_node = TreeNode(1)
fourth_node = TreeNode(2)
fifth_node = TreeNode(5)
sixth_node = TreeNode(6)

first_node.left = second_node
first_node.right = fifth_node
second_node.left = third_node
second_node.right = fourth_node
fifth_node.right = sixth_node

root = first_node

obj = ConvertTreeLinkedList()
res = obj.convert_tree_to_linked_list(root)
obj.printList(res)

# Time Complexity: O(n)
# Space Complexity: O(n)