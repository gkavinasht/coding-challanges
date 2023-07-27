# 658. Find K Closest Elements
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
# An integer a is closer to x than an integer b if:
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b

def findClosestElements(arr, k, x):
    diff = []
    for num in arr:
        diff.append((num, abs(x - num)))

    diff.sort(key = lambda x: x[1])
    res = [i[0] for i in diff[:k]]
    return sorted(res)

arr = [1,2,3,4,5]
k = 4
x = 3
print(findClosestElements(arr, k, x))

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# Output: [1,2,3,4]