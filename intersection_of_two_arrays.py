# 349. Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

def intersection(nums1, nums2):
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    p1, p2 = 0, 0
    res = set()

    while p1 < len(nums1) and p2 < len(nums2):
        val1 = nums1[p1]
        val2 = nums2[p2]

        if val1 == val2:
            res.add(val1)
            p1 += 1 # Can increment either p1 or p2
        elif val1 < val2:
            p1 += 1
        elif val1 > val2:
            p2 += 1
    return res

    # Time Complexity: O(mlogm+nlogn) - for sorting (nlogn), for iterating (n)
    # Space Complexity: O(m+n)

    # res = set()
    # num1Set = set(nums1)

    # for num in nums2:
    #     if num in num1Set:
    #         res.add(num)
    # return res

    # Time Complexity: O(m+n)
    # Space Complexity: O(m+n)

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1, nums2))

# Output: [2]