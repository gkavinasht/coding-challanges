# 797. All Paths From Source to Target
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

def allPathsSourceTarget(graph):
    # BFS
    paths = []
    queue = collections.deque([(0, [0])])

    while queue:
        node, path = queue.popleft()

        if node == len(graph) - 1:
            paths.append(list(path))

        for nei in graph[node]:
            queue.append((nei, path + [nei]))

    return paths

    # DFS
    # def dfs(node, path):
    #     if node == n - 1:
    #         paths.append(list(path))
    #         return

    #     for nei in graph[node]:
    #         path.append(nei)
    #         dfs(nei, path)
    #         path.pop()

    # n = len(graph)
    # paths = []
    # dfs(0,[0])
    # return paths

graph = [[1,2],[3],[3],[]]
print(allPathsSourceTarget(graph))

# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

# Time Complexity: O(2**n)
# Space Complexity: O(2**n)