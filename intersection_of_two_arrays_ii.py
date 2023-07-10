# 350. Intersection of Two Arrays II
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

def intersect(nums1, nums2):
    res = []
    nums1dict = {}

    for num in nums1:
        nums1dict[num] = nums1dict.get(num, 0) + 1

    for num in nums2:
        if num in nums1dict and nums1dict[num] > 0:
            res.append(num)
            nums1dict[num] -= 1
    return res

nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersect(nums1, nums2))

# Time Complexity: O(m + n)
# Space Complexity: O(n)

# Output: [2,2]