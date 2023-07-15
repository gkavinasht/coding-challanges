# 215. Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

import heapq

def findKthLargest(nums, k):
	# Min Heap
    # heap = []
    # for num in nums:
    #     heapq.heappush(heap, num)
    #     if len(heap) > k:
    #         heapq.heappop(heap)

    # return heap[0]

    # Time Complexity: O(nlogk)
    # Space Complexity: O(k) -> Heap

    numsdict = {}
    minVal, maxVal = min(nums), max(nums)

    for num in nums:
        numsdict[num] =  numsdict.get(num, 0) + 1

    index = 0
    for val in range(minVal, maxVal + 1):
        while numsdict.get(val, 0) > 0:
            nums[index] = val
            if index == len(nums) - k:
                return nums[index]
            numsdict[val] -= 1
            index += 1
    return -1

    # Counting Sort
    # Time Complexity: O(n + m)
    # Space Complexity: O(m)

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))
# Output: 5