# 454. 4Sum II
# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

def fourSumCount(nums1, nums2, nums3, nums4):
    sums, res = defaultdict(int), 0

    for x in nums1:
        for y in nums2:
            sums[x + y] += 1

    for i in nums3:
        for j in nums4:
            res += sums[0 - (i + j)]

    return res

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]

print(fourSumCount(nums1, nums2, nums3, nums4))

# Time Complexity: O(n**2)
# Space Complexity: O(n**2)

# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0