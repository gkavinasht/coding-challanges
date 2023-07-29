# 287. Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

def findDuplicate(nums):
	l, r = 1, len(nums) - 1
        
    while l <= r:
        cur = (l + r) // 2
        count = 0

        # Count how many numbers are less than or equal to 'cur'
        count = sum(num <= cur for num in nums)
        if count > cur:
            duplicate = cur
            r = cur - 1
        else:
            l = cur + 1
            
    return duplicate

    # Time Complexity: O(logn)
	# Space Complexity: O(1)

    # numsdict = {}
    # for i in nums:
    #     if i in numsdict:
    #         return i
    #     numsdict[i] = 1

    # Time Complexity: O(n)
	# Space Complexity: O(n)

nums = [1,3,4,2,2]
print(findDuplicate(nums))

# Output: 2