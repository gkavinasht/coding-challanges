# 1192. Critical Connections in a Network
# There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.
# A critical connection is a connection that, if removed, will make some servers unable to reach some other server. Return all critical connections in the network in any order.

import collections
def criticalConnections(n, connections):
	graph = collections.defaultdict(list)
	for u, v in connections:
	    graph[u].append(v)
	    graph[v].append(u)

	# min_discovery_time of nodes at respective indices from start node
	# 1. default to max which is the depth of continuous graph
	lows = [n] * n
	critical = []

	def dfs(node, discovery_time, parent): 
	    # if the low is not yet discovered for this node
	    if lows[node] == n:
	        
	        # 2. default it to the depth or discovery time of this node
	        lows[node] = discovery_time
	        
	        for neighbor in graph[node]:
	            # all neighbors except parent
	            if neighbor != parent:
	                expected_discovery_time_of_child = discovery_time + 1
	                actual_discovery_time_of_child = dfs(neighbor, expected_discovery_time_of_child, node)
	                
	                # nothing wrong - parent got what was expected => no back path
	                # this step is skipped if there is a back path
	                if actual_discovery_time_of_child >= expected_discovery_time_of_child:
	                    critical.append((node, neighbor))
	                
	                # low will be equal to discovery time of this node or discovery time of child
	                # whichever one is minm
	                # if its discovery time of child - then there is a backpath
	                lows[node] = min(lows[node], actual_discovery_time_of_child)
	                
	    # return low of this node discovered previously or during this call 
	    return lows[node]

	dfs(n - 1, 0, -1)
	return critical

n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
print(criticalConnections(n, connections))

# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)