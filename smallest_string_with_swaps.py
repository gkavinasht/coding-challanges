# 1202. Smallest String With Swaps
# You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
# You can swap the characters at any pair of indices in the given pairs any number of times.
# Return the lexicographically smallest string that s can be changed to after using the swaps.

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    # Path Compression
    def find(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
 
def smallestStringWithSwaps(s, pairs):
    n = len(s)
    uf = UnionFind(n)

    # Union connected pairs
    for a, b in pairs:
        uf.union(a, b)

    # Group characters within the same connected component
    components = {}
    for i in range(n):
        root = uf.find(i)
        if root in components:
            components[root].append(s[i])
        else:
            components[root] = [s[i]]

    # Sort characters lexicographically within each group
    for root in components:
        components[root].sort(reverse=True)

    # Reconstruct the string
    result = []
    for i in range(n):
        root = uf.find(i)
        result.append(components[root].pop())

    return "".join(result)

s = "dcab"
pairs = [[0,3],[1,2]]
print(smallestStringWithSwaps(s, pairs))

# Output: "bacd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"

# Time Complexity: O(nlog(n))
# Space Complexity: O(n)