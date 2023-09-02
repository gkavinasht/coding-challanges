# 547. Number of Provinces
# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

def findCircleNum(isConnected):
    # DFS Approach
    def dfs(i):
        visited[i] = True
        
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and not visited[j]:
                dfs(j)

    visited = [False] * len(isConnected)
    provinces = 0

    for i in range(len(isConnected)):
        if not visited[i]:
            dfs(i)
            provinces += 1

    return provinces

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(findCircleNum(isConnected))

# Output: 2

# Time Complexity: O(n^2)
# Space Complexity: O(n)