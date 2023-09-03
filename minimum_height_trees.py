# 310. Minimum Height Trees
# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
# Return a list of all MHTs' root labels. You can return the answer in any order.
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

import collections
def findMinHeightTrees(n, edges):
        # def treeHeight(root):
        #     stack = collections.deque([(root, 0)])
        #     level = 0
        #     visited = set()

        #     while stack:
        #         curr_node, curr_level = stack.popleft()
        #         visited.add(curr_node)

        #         for children in graph[curr_node]:
        #             if children not in visited:
        #                 stack.append((children, curr_level + 1))
        #                 level = curr_level + 1
        #     return level

        # graph = defaultdict(list)
        # min_height = float('inf')
        # min_trees = []
        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)

        # for i in range(n):
        #     curr_height = treeHeight(i)
        #     if curr_height < min_height:
        #         min_trees = [i]
        #         min_height = curr_height
        #     elif curr_height == min_height:
        #         min_trees.append(i)

        # return min_trees

        # Time Complexity: O(V + E)
		# Space Complexity: O(V + E)

        # Topological Sort
        # edge cases
        if n <= 2:
            return [i for i in range(n)]

        neighbors = collections.defaultdict(set)
        for u, v in edges:
            neighbors[u].add(v)
            neighbors[v].add(u)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves

        # Time Complexity: O(V)
		# Space Complexity: O(V)

n = 4
edges = [[1,0],[1,2],[1,3]]
print(findMinHeightTrees(n, edges))

# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.