# 1615. Maximal Network Rank
# There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.
# The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.
# The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.
# Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

import collections
def maximalNetworkRank(n, roads):
    graph = collections.defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
    
    max_rank = 0
    for i in range(n):
        for j in range(i + 1, n):
            rank_i = len(graph[i])
            rank_j = len(graph[j])
            curr_rank = rank_i + rank_j
            if j in graph[i]:
                curr_rank -= 1
            max_rank = max(max_rank, curr_rank)

    return max_rank

n = 4
roads = [[0,1],[0,3],[1,2],[1,3]]
print(maximalNetworkRank(n, roads))

# Time Complexity: O(E + V**2)
# Space Complexity: O(E)

# Output: 4
# Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.