# 323. Number of Connected Components in an Undirected Graph
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

import collections
def connected_components(n, edges):
	def dfs(root):
		if root in visited:
			return

		visited.add(root)
		for node in graph[root]:
			if node not in visited:
				dfs(node)

	graph = collections.defaultdict(list)
	for i in range(len(edges)):
		start, end = edges[i]
		graph[start].append(end)
		graph[end].append(start)

	visited = set()
	components = 0
	for i in range(n):
		if i not in visited:
			dfs(i)
			components += 1
	return components

n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(connected_components(n, edges))

# Output: 2

# Time Complexity: O(m + n) -> m is no. of edges
# Space Complexity: O(m + n)