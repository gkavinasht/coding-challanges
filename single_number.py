# 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber(nums):
    a = 0
    for num in nums:
        a ^= num
    return a

    # Time Complexity: O(n)
	# Space Complexity: O(1)
    
    # numDict = {}
    # for num in nums:
    #     numDict[num] = numDict.get(num, 0) + 1

    # for key, val in numDict.items():
    #     if val == 1:
    #         return key

    # Time Complexity: O(n)
	# Space Complexity: O(n)

nums = [2,2,1]
print(singleNumber(nums))

# Output: 1