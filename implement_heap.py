# Implement Heap
# Min Heap
class MinHeap:
	def __init__(self, heapSize):
		# Create a complete binary tree using an array
	    # Then use the binary tree to construct a Heap
		self.heapSize = heapSize

		# the number of elements is needed when instantiating an array
	    # heapSize records the size of the array
		self.minheap = [0] * (heapSize + 1)

		# realSize records the number of elements in the Heap
		self.realSize = 0

	# Add an element
	def add(self, element):
		self.realSize += 1

		# If the number of elements in the Heap exceeds the preset heapSize
		if self.realSize > self.heapSize:
			print("Added too may elements")
			self.realSize -= 1
			return

		# Add the element into the array
		self.minheap[self.realSize] = element

		# Index of the newly added element
		index = self.realSize

		# Parent node of the newly added element
		parent = index // 2

		# If the newly added element is smaller than its parent node,
	    # its value will be exchanged with that of the parent node 
		while self.minheap[index] < self.minheap[parent] and index > 1:
			self.minheap[parent], self.minheap[index] = self.minheap[index], self.minheap[parent]
			index = parent
			parent = index // 2

	# Get the top element of the Heap
	def peek(self):
		return self.minheap[1]

	# Delete the top element of the Heap
	def pop(self):
		# If the number of elements in the current Heap is 0
		if self.realSize < 1:
			print("Don't have any element")
			return sys.maxsize
		else:
			# When there are still elements in the Heap
			removeElement = self.minheap[1]

			# Put the last element in the Heap to the top of Heap
			self.minheap[1] = self.minheap[self.realSize]
			self.realSize -= 1
			index = 1

			# When the deleted element is not a leaf node
			while index <= self.realSize // 2:
				# the left child of the deleted element
				left = index * 2
				# the right child of the deleted element
				right = (index * 2) + 1

				# If the deleted element is larger than the left or right child
	            # its value needs to be exchanged with the smaller value
	            # of the left and right child
				if self.minheap[index] > self.minheap[left] or self.minheap[index] > self.minheap[right]:
					if self.minheap[left] < self.minheap[right]:
						self.minheap[left], self.minheap[index] = self.minheap[index], self.minheap[left]
						index = left
					else:
						self.minheap[right], self.minheap[index] = self.minheap[index], self.minheap[right]
						index = right
				else:
					break
			return removeElement

	# return the number of elements in the Heap
	def size(self):
	    return self.realSize

	def __str__(self):
		return str(self.minheap[1 : self.realSize + 1])

minHeap = MinHeap(5)
minHeap.add(3)
minHeap.add(1)
minHeap.add(2)
# [1,3,2]
print(minHeap)
# 1
print(minHeap.peek())
# 1
print(minHeap.pop())
# 2
print(minHeap.pop())
# 3
print(minHeap.pop())
minHeap.add(4)
minHeap.add(5)
# [4,5]
print(minHeap)
# 4
print(minHeap.pop())
# 5
print(minHeap.pop())


# Max Heap
class MaxHeap:
	def __init__(self, heapSize):
		# Create a complete binary tree using an array
	    # Then use the binary tree to construct a Heap
		self.heapSize = heapSize

		# the number of elements is needed when instantiating an array
	    # heapSize records the size of the array
		self.maxheap = [0] * (heapSize + 1)

		# realSize records the number of elements in the Heap
		self.realSize = 0

	# Add an element
	def add(self, element):
		self.realSize += 1

		# If the number of elements in the Heap exceeds the preset heapSize
		if self.realSize > self.heapSize:
			print("Added too may elements")
			self.realSize -= 1
			return

		# Add the element into the array
		self.maxheap[self.realSize] = element

		# Index of the newly added element
		index = self.realSize

		# Parent node of the newly added element
		parent = index // 2

		# If the newly added element is larger than its parent node,
	    # its value will be exchanged with that of the parent node 
		while self.maxheap[index] > self.maxheap[parent] and index > 1:
			self.maxheap[parent], self.maxheap[index] = self.maxheap[index], self.maxheap[parent]
			index = parent
			parent = index // 2

	# Get the top element of the Heap
	def peek(self):
		return self.maxheap[1]

	# Delete the top element of the Heap
	def pop(self):
		# If the number of elements in the current Heap is 0
		if self.realSize < 1:
			print("Don't have any element")
			return sys.maxsize
		else:
			# When there are still elements in the Heap
			removeElement = self.maxheap[1]

			# Put the last element in the Heap to the top of Heap
			self.maxheap[1] = self.maxheap[self.realSize]
			self.realSize -= 1
			index = 1

			# When the deleted element is not a leaf node
			while index <= self.realSize // 2:
				# the left child of the deleted element
				left = index * 2
				# the right child of the deleted element
				right = (index * 2) + 1

				# If the deleted element is smaller than the left or right child
	            # its value needs to be exchanged with the larger value
	            # of the left and right child
				if self.maxheap[index] < self.maxheap[left] or self.maxheap[index] < self.maxheap[right]:
					if self.maxheap[left] > self.maxheap[right]:
						self.maxheap[left], self.maxheap[index] = self.maxheap[index], self.maxheap[left]
						index = left
					else:
						self.maxheap[right], self.maxheap[index] = self.maxheap[index], self.maxheap[right]
						index = right
				else:
					break
			return removeElement

	# return the number of elements in the Heap
	def size(self):
	    return self.realSize

	def __str__(self):
		return str(self.maxheap[1 : self.realSize + 1])

maxHeap = MaxHeap(5)
maxHeap.add(1)
maxHeap.add(2)
maxHeap.add(3)
# [3,1,2]
print(maxHeap)
# 3
print(maxHeap.peek())
# 3
print(maxHeap.pop())
# 2
print(maxHeap.pop())
# 1
print(maxHeap.pop())
maxHeap.add(4)
maxHeap.add(5)
# [5,4]
print(maxHeap)
# 5
print(maxHeap.pop())
# 4
print(maxHeap.pop())


# Time Complexities:
# Min/Max Heap:
# Add - O(logn), Pop - O(logn), Peek - O(1)

# Space Complexities:
# Min/Max Heap:
# Add, Pop, Peek - O(1)