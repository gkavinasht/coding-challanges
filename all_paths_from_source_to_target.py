# 797. All Paths From Source to Target
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

def allPathsSourceTarget(graph):
    def dfs(root, path):
        if root == len(graph) - 1:
            paths.append(list(path))
            return

        for children in graph[root]:
            path.append(children)
            dfs(children, path)
            path.pop()

    paths = []
    dfs(0, [0])
    return paths

graph = [[1,2],[3],[3],[]]
print(allPathsSourceTarget(graph))

# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

# Time Complexity: O(2**n)
# Space Complexity: O(2**n)