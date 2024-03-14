"""
1971. Find if Path Exists in Graph
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
"""

def validPath(n, edges, source, destination):
    # BFS
    graph = collections.defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = collections.deque([source])
    visited = set()
    visited.add(source)

    while queue:
        node = queue.popleft()

        if node == destination:
            return True

        for nei in graph[node]:
            if nei not in visited:
                queue.append(nei)
                visited.add(nei)

    return False

    # DFS
    # graph = collections.defaultdict(list)
    # for u, v in edges:
    #     graph[u].append(v)
    #     graph[v].append(u)

    # def dfs(node, visited):
    #     visited.add(node)

    #     if node == destination:
    #         return True

    #     for nei in graph[node]:
    #         if nei not in visited:
    #             if dfs(nei, visited):
    #                 return True

    #     return False

    # visited = set()
    # if dfs(source, visited):
    #     return True

    # return False