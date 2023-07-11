# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def topKFrequent(nums, k):
    numsdict = {}
    for num in nums:
        numsdict[num] = numsdict.get(num, 0) + 1

    # Store numsk with elements in highest to lowest freq
    # numsk = sorted(numsdict, key = lambda x: (-numsdict[x], x))
    # return numsk[:k]

    # Time Complexity: O(nlogn) - Built-in sort
    # Space Complexity: O(n)

    # Heaps
    heap = []
    for key in numsdict:
        # Max Heap - Push (freq, ele) to heap in highest to lowest freq 
        heapq.heappush(heap, (-numsdict[key], key))

    res = []
    for _ in range(k):
        # Pop top element and extract element at index 1
        popped_element = heapq.heappop(heap)[1]
        res.append(popped_element)

    return res

    # Time Complexity: O(nlogk) - Heap Construction - O(nlogk), Heap Extraction - O(klogk)
    # Space Complexity: O(n) - Dictionary, Heap

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
# Output: [1,2]