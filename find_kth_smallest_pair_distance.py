# 719. Find K-th Smallest Pair Distance
# The distance of a pair of integers a and b is defined as the absolute difference between a and b.
# Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

def smallestDistancePair(self, nums: List[int], k: int) -> int:
    n = len(nums)
    nums.sort()
    heap = []

    for i in range(n-1):
        heapq.heappush(heap, (nums[i + 1] - nums[i], i, i + 1))

    for _ in range(k):
        d, root, nei = heapq.heappop(heap)
        # To add the difference between the elements occuring after right element and the left element
        if nei + 1 < n:
            heapq.heappush(heap, (nums[nei + 1] - nums[root], root, nei + 1))
    return d

    # Time Complexity: O(klogn + nlogn)
    # Space Complexity: O(n)

nums = [1,3,1]
k = 1
print(smallestDistancePair(nums, k))

# Output: 0
# Explanation: Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.