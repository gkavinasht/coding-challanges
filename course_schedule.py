# 207. Course Schedule
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

import collections

def canFinish(numCourses, prerequisites):
    def hasCycle(root):
        if states[root] == EXPLORING:
            return True
        if states[root] == DONE:
            return False

        # Mark the course as visiting.
        states[root] = EXPLORING
        for node in graph[root]:
            if hasCycle(node):
                return True

        states[root] = DONE
        return False

    graph = collections.defaultdict(list)
    for i in range(len(prerequisites)):
        a, b = prerequisites[i]
        graph[a].append(b)

    # 3 possible states for a course: not visited - 0, visiting - 1, visited - 2
    states = [0] * numCourses
    UNVISITED, EXPLORING, DONE = 0, 1, 2

    # Check for cycles (if there's a cycle, all courses cannot be finished)
    for i in range(numCourses):
        if states[i] == 0:
            if hasCycle(i):
                return False

    return True

numCourses = 2
prerequisites = [[1,0]]
print(canFinish(numCourses, prerequisites))

# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Time Complexity: O(V * E)
# Space Complexity: O(V)