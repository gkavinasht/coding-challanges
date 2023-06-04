# 941. Valid Mountain Array
"""
Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""

def validMountainArray(arr):
    n = len(arr) - 1
    if n < 2:
        return False

    if arr[1] < arr[0]:
        return False
    
    i = 1
    increasing = True
    while i <= n:
        if arr[i] == arr[i - 1]:
            return False
        if increasing == True:
            if arr[i] < arr[i - 1]:
                increasing = False
        else:
            if arr[i] > arr[i - 1]:
                return False
        i += 1
    if increasing == True:
        return False
    return True

arr = [0,3,2,1]
print(validMountainArray(arr))

# Output: true

# Time Complexity: O(n)
# Space Complexity: O(1)