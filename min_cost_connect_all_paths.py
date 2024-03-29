"""
1584. Min Cost to Connect All Points
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
"""

class UnionFind:
    def __init__(self, size):
        self.group = [0] * size
        self.rank = [0] * size

        for i in range(size):
            self.group[i] = i
      
    def find(self, node):
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def join(self, node1: int, node2: int) -> bool:
        group1 = self.find(node1)
        group2 = self.find(node2)
        
        # node1 and node2 already belong to same group.
        if group1 == group2:
            return False

        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1

        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's Algorithm
        n = len(points)

        # Min-heap to store minimum weight edge at top.
        heap = [(0, 0)]

        # Track nodes which are included in MST.
        in_mst = [False] * n

        mst_cost = 0
        edges_used = 0

        while edges_used < n:
            weight, curr_node = heapq.heappop(heap)

            # If node was already included in MST we will discard this edge.
            if in_mst[curr_node]:
                continue

            in_mst[curr_node] = True
            mst_cost += weight
            edges_used += 1

            for next_node in range(n):
                # If next node is not in MST, then edge from curr node
                # to next node can be pushed in the priority queue.
                if not in_mst[next_node]:
                    next_weight = abs(points[curr_node][0] - points[next_node][0]) + abs(points[curr_node][1] - points[next_node][1])

                    heapq.heappush(heap, (next_weight, next_node))

        return mst_cost

        # Time complexity: O(N^2⋅log(N))
        # Space complexity: O(N^2)

        # Krushkal's Algorithm
        # n = len(points)
        # all_edges = []

        # # Storing all edges of our complete graph.
        # for curr_node in range(n):
        #     for next_node in range(curr_node + 1, n):
        #         weight = abs(points[curr_node][0] - points[next_node][0]) + abs(points[curr_node][1] - points[next_node][1])

        #         all_edges.append((weight, curr_node, next_node))

        # # Sort all edges in increasing order.
        # all_edges.sort()

        # uf = UnionFind(n)

        # mst_cost = 0
        # edges_used = 0

        # for weight, node1, node2 in all_edges:
        #     if uf.join(node1, node2):
        #         mst_cost += weight
        #         edges_used += 1
        #         if edges_used == n - 1:
        #             break

        # return mst_cost

        # Time complexity: O(N^2⋅log(N))
        # Space complexity: O(N^2)