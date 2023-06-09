# 1089. Duplicate Zeros
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    possible_dups = 0
    length = len(arr) - 1

    # Find the number of zeros to be duplicated
    for left in range(length + 1):
        # Stop when left points beyond the last element in the original list which would be part of modified list
        if left > length - possible_dups:
            break

        # Count zeros
        if arr[left] == 0:
            # Edge case: This zero cannot be duplicated. We have no more space, as left is pointing to the last element which could be included in the modified list
            if left == length - possible_dups:
                arr[length] = 0
                length -= 1
                break
            possible_dups += 1

    # Start backwards from the last element which could be included in the modified list
    last = length - possible_dups

    # Copy zero twice and non zero once
    for i in range(last, -1, -1):
        if arr[i] == 0:
            arr[i + possible_dups] = 0
            possible_dups -= 1
            arr[i + possible_dups] = 0
        else:
            arr[i + possible_dups] = arr[i]

arr = [1,0,2,3,0,4,5,0]
duplicateZeros(arr)
print(arr)

# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

# Time Complexity : O(n)
# Space Complexity: O(1)