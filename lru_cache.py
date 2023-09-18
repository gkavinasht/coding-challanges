# 146. LRU Cache
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. 
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key. 
# The functions get and put must each run in O(1) average time complexity.

# Using Double Linked list and HashMap
import collections
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
	def __init__(self, capacity: int):
		self.cache = collections.defaultdict(int)
		self.capacity = capacity
		self.head = ListNode()
		self.tail = ListNode()
		self.head.next = self.tail
		self.tail.prev = self.head

	def add_node(self, node):
		# Add a node to the front of the linked list
		node.prev = self.head
		node.next = self.head.next
		self.head.next.prev = node
		self.head.next = node

	def remove_node(self, node):
		# Remove a node from the linked list
		prev = node.prev
		next_node = node.next
		prev.next = next_node
		next_node.prev = prev

	def move_to_front(self, node):
		# Move a node to the front of the linked list
		self.remove_node(node)
		self.add_node(node)

	def pop_tail(self):
		# Remove and return the tail node from the linked list
		tail = self.tail.prev
		self.remove_node(tail)
		return tail

	def get(self, key: int) -> int:
		if key in self.cache:
			node = self.cache[key]
			# Move the recently used node to front
			self.move_to_front(node)
			return node.value
		return -1

	def put(self, key: int, value: int) -> None:
		if key in self.cache:
			# If the key exists, update its value and move it to the front
			node = self.cache[key]
			node.value = value
			# Move the recently used node to front
			self.move_to_front(node)
		else:
			if len(self.cache) >= self.capacity:
				# If the cache is full, remove the least recently used item
				tail = self.pop_tail()
				del self.cache[tail.key]
			# Add the new key-value pair to the cache and the linked list
			new_node = ListNode(key, value)
			self.cache[key] = new_node
			self.add_node(new_node)


# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
capacity = 2
lrucache = LRUCache(capacity)
lrucache.put(1, 1)
lrucache.put(2, 2)
print(lrucache.get(1))
lrucache.put(3, 3)
print(lrucache.get(2))
lrucache.put(4, 4)
print(lrucache.get(1))
print(lrucache.get(3))
print(lrucache.get(4))

# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]