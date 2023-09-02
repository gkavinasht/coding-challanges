# 261. Graph Valid Tree
# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

import collections
def isValidTree(n, edges):
	def dfs(root):
		visited.add(root)

		for node in graph[root]:
			if node in visited:
				continue
			dfs(node)

	graph = collections.defaultdict(list)
	for i in range(len(edges)):
		start, end = edges[i]
		graph[start].append(end)
		graph[end].append(start)

	visited = set()
	dfs(0)
	return len(visited) == n and len(edges) == n - 1

n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]
print(isValidTree(n , edges))

# Output: true

# Time Complexity: O(m + n) -> m is no. of edges
# Space Complexity: O(m + n)