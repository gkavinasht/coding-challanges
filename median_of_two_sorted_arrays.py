# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

def findMedianSortedArrays(nums1, nums2):
    # Merge Sort
    # m, n = len(nums1), len(nums2)
    # i, j, k = 0, 0, 0
    # merged = [0] * (m + n)

    # while i < m and j < n:
    #     if nums1[i] <= nums2[j]:
    #         merged[k] = nums1[i]
    #         i += 1
    #     else:
    #         merged[k] = nums2[j]
    #         j += 1
    #     k += 1

    # while i < m:
    #     merged[k] = nums1[i]
    #     i += 1
    #     k += 1

    # while j < n:
    #     merged[k] = nums2[j]
    #     j += 1
    #     k += 1

    # if len(merged) % 2 == 0:
    #     median = (merged[(len(merged) // 2) - 1] + merged[len(merged) // 2]) / 2
    # else:
    #     median = merged[(len(merged) // 2)]

    # return median

    # Time Complexity: O(m + n)
    # Space Complexity: O(n)

    # Binary Search
    m = len(nums1)
    n = len(nums2)
    
    if m > n:
        return findMedianSortedArrays(nums2, nums1)
    
    low = 0
    high = m
    while low <= high:
        partitionA = (low + high) // 2
        partitionB = ((m + n + 1) // 2) - partitionA
        
        maxLeftA = float('-inf') if partitionA == 0 else nums1[partitionA - 1]
        minRightA = float('inf') if partitionA == m else nums1[partitionA]
        
        maxLeftB = float('-inf') if partitionB == 0 else nums2[partitionB - 1]
        minRightB = float('inf') if partitionB == n else nums2[partitionB]
        
        if maxLeftA <= minRightB and maxLeftB <= minRightA:
            if (m + n) % 2 == 0:
                return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
            else:
                return max(maxLeftA, maxLeftB)
            
        elif maxLeftA > minRightB:
            high = partitionA - 1
        else:
            low = partitionA + 1

    # Time Complexity: O(log(min(m,n)))
    # Space Complexity: O(1)


nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))

# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.