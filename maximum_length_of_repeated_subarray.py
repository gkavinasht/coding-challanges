# 718. Maximum Length of Repeated Subarray
# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

def findLength(nums1, nums2):
    m, n = len(nums1), len(nums2)
    max_len = 0

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if nums1[i] == nums2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
                max_len = max(max_len, dp[i][j])
    return max_len

nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
print(findLength(nums1, nums2))

# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)