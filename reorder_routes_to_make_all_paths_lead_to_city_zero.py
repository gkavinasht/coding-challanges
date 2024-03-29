# 1466. Reorder Routes to Make All Paths Lead to the City Zero
# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.
# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi. This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed. It's guaranteed that each city can reach city 0 after reorder.

import collections
class Solution:
    def __init__(self):
        self.count = 0

    def dfs(self, node, parent, graph):
        if node not in graph:
            return

        for child, sign in graph[node]:
            if child != parent:
                self.count += sign
                self.dfs(child, node, graph)

    def minReorder(self, n, connections):
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1)) # Original Edge from connections
            graph[v].append((u, 0)) # Artificial Edge, opposite to connections

        self.dfs(0, -1, graph)
        return self.count

n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
s= Solution()
print(s.minReorder(n, connections))

# Output: 3
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

# Time Complexity: O(n)
# Space Complexity: O(n)