"""
You will be given an integer array and a threshold value. The threshold represents the maximum length of subarrays that may be created for the challenge. Each subarray created has a cost equal to the maximum integer within the subarray. Partition the entire array into subarrays with lengths less than or equal to the threshold, and do it at a minimum cost. The subarrays are to be chosen from contiguous elements, and the given array must remain in its original order.

Ex: [1, 3, 4, 5, 2, 6] threshold = 3
Partition into 6 subarrays: [1], [3], [4], [5], [2], [6] Cost: 1+3+4+5+2+6=21
Partition into 3 subarrays: [1,3], [4,5], [2,6] Cost: 3+5+6=14
Partition into 2 subarrays: [1,3,4], [5,2,6] Cost: 4+6=10
The optimal cost is 10.
"""

def minCostToPartition(arr, threshold):
    n = len(arr)
    dp = [float('inf')] * (n + 1)
    dp[n] = 0
    
    for ind in range(n - 1, -1, -1):
        max_ele = 0
        for i in range(ind, min(ind + threshold, n)):
            max_ele = max(max_ele, arr[i])
            dp[ind] = min(dp[ind], max_ele + dp[i + 1])
            
    return dp[0]

arr = [1, 3, 4, 5, 2, 6]
threshold = 3
result = minCostToPartition(arr, threshold)
print(result) # 10