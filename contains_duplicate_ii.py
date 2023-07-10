# 219. Contains Duplicate II
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

def containsNearbyDuplicate(nums, k):
    numsdict = {}
    for i in range(len(nums)):
        if nums[i] in numsdict:
            if abs(i - numsdict[nums[i]]) <= k:
                return True
        numsdict[nums[i]] = i
    return False

nums = [1,2,3,1]
k = 3

# Output: true