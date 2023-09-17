# 1248. Count Number of Nice Subarrays
# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.

def numberOfSubarrays(nums, k):
    start = 0
    odd_count, curr_sub_count = 0, 0
    res = 0

    for end in range(len(nums)):
        if nums[end] % 2 != 0:
            odd_count += 1
            curr_sub_count = 0
        while odd_count == k:
            curr_sub_count += 1
            if nums[start] % 2 != 0:
                odd_count -= 1
            start += 1
        res += curr_sub_count

    return res

nums = [1,1,2,1,1]
k = 3
print(numberOfSubarrays(nums, k))

# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

# Time Complexity: O(n)
# Space Complexity: O(1)