# 96. Unique Binary Search Trees
# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

def numTrees(n):
	numTrees = [1] * (n + 1)

	# 0 nodes = 1 tree
	# 1 nodes = 1 tree
	for nodes in range(2, n + 1):
		total = 0
		for root in range(1, nodes + 1):
			left = root - 1
			right = nodes - root
			total += (numTrees[left] * numTrees[right])
		numTrees[nodes] = total
	return numTrees[n]

n = 3
print(numTrees(n))
# Output: 5

# Time Complexity: O(n**2)
# Space Complexity: O(n)