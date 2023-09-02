# 399. Evaluate Division
# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

import collections

def calcEquation(equations, values, queries):
    graph = collections.defaultdict(dict)
    for i in range(len(equations)):
        A, B = equations[i]
        graph[A][B] = values[i]
        graph[B][A] = 1 / values[i]

    def dfs(start, end, visited):
        if start not in graph or end not in graph:
            return -1.0

        if start == end:
            return 1.0

        visited.add(start)

        for neighbhor, weight in graph[start].items():
            if neighbhor not in visited:
                result = dfs(neighbhor, end, visited)
                if result != -1.0:
                    return result * weight

        visited.remove(start)
        return -1.0

    results = []
    for i in range(len(queries)):
        C, D = queries[i]
        visited = set()
        result = dfs(C, D, visited)
        results.append(result)
    
    return results

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(calcEquation(equations, values, queries))

# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0

# Time Complexity: O(m * n)
# Space Complexity: O(n)