# 410. Split Array Largest Sum
# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized. Return the minimized largest sum of the split. A subarray is a contiguous part of the array.

def splitArray(nums, k):
    '''
    statement : algorithm to minimize the largest sum among these m subarrays.

    1.  set low and high limits of ( minimum largest sum)
    2.  condition for reaching to possible answer

    if subarrays are more than m ,then we need large (min large sum) ,left = mid+1

    '''
    low = max(nums)
    high = sum(nums)

    while low <= high:
    	possible = (low + high) // 2

    	# To check if it is possible to partition nums into k sub-arrays
    	def isValid(possible):
    		subarrays = 1
    		runningSum = 0

    		for num in nums:
    			runningSum += num
    			# If running sum is exceeding possible, increment sub array and reset running sum to current num
    			if runningSum > possible:
    				subarrays += 1
    				runningSum = num
    		# Return True/False if subarrays is less than or equal to k
    		return subarrays <= k

    	if isValid(possible):
    		# To search for smaller value than possible
    		high = possible - 1
    	else:
    		# To search for larger value than possible
    		low = possible + 1

    return low

nums = [7,2,5,10,8]
k = 2
print(splitArray(nums, k))

# Time Complexity: O(nlogs) -> n - number of elements, s - sum of elemets
# Space Complexity: O(1)

# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.