# 1299. Replace Elements with Greatest Element on Right Side
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
# After doing so, return the array.

def replaceElements(arr):
    maximum = -1
    i = len(arr) - 1 
    while i >= 0:
        temp = arr[i]
        arr[i] = maximum
        maximum = max(maximum, temp)
        i -= 1
    return arr

    # n = len(arr) - 1
    # i = len(arr) - 2
    # maximum = arr[n]
    # previous = current = 0
    # while i >= 0:
    #     current = arr[i]
    #     arr[i] = max(previous, maximum)
    #     maximum = arr[i]
    #     previous = current
    #     i -= 1
    # arr[n] = -1
    # return arr

arr = [17,18,5,4,6,1]
print(replaceElements(arr))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.