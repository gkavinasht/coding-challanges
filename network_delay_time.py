"""
743. Network Delay Time
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
"""

def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        queue = [(0, k)] # (cost, node)
        visited = set()
        max_cost = 0

        while queue:
            cost, node = heapq.heappop(queue)

            if node in visited:
                continue

            visited.add(node)
            max_cost = max(max_cost, cost)
            
            for nei in graph[node]:
                new_node, new_cost = nei
                if new_node not in visited:
                    curr_cost = cost + new_cost

                    heapq.heappush(queue, (curr_cost, new_node))

        return max_cost if len(visited) == n else -1

        # Time Complexity: O(E + V log V)
        # Space Complexity: O(V)