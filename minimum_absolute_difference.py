# 1200. Minimum Absolute Difference
# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr

def minimumAbsDifference(arr):
    arr = sorted(arr)
    min_diff = float('inf')
    res = []

    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i - 1])
        if diff < min_diff:
            min_diff = diff
            res.clear()
            res.append([arr[i - 1], arr[i]])
        elif min_diff == diff:
            res.append([arr[i - 1], arr[i]])

    return res

arr = [4,2,1,3]
print(minimumAbsDifference(arr))

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.