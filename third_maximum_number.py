# 414. Third Maximum Number
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

import heapq

def thirdMax(nums):
	# Three variables to store maxiumum three numbers till now.
    first_max = -inf
    second_max = -inf
    third_max = -inf

    for num in nums:
        # This number is already used once, thus we skip it.
        if first_max == num or second_max == num or third_max == num:
            continue

        # If current number is greater than first maximum,
        # It means that this is the greatest number and first max and second max
        # will become the next two greater numbers.
        if num >= first_max:
            third_max = second_max
            second_max = first_max
            first_max = num
        # When current number is greater than second maximum,
        # it means that this is the second greatest number.
        elif num >= second_max:
            third_max = second_max
            second_max = num
         # It is the third greatest number.
        elif third_max <= num:
            third_max = num
    
    # If third max was never updated, it means we don't have 3 distinct numbers.
    if third_max == -inf:
        return first_max
    
    return third_max

    # Time Complexity: O(n)
	# Space Complexity: O(1)
	
	# Min Heap
	# min_heap = []
	# hash_set = set()

	# for i in range(len(nums)):
	#     # If current number was already taken, skip it.
	#     if nums[i] in hash_set:
	#         continue

	#     # If min heap already has three numbers in it.
	#     # Pop the smallest if current number is bigger than it.
	#     if len(min_heap) == 3:
	#         if min_heap[0] < nums[i]:
	#             hash_set.remove(min_heap[0])
	#             heapq.heappop(min_heap)

	#             heapq.heappush(min_heap, nums[i])
	#             hash_set.add(nums[i])
	#     # If min heap does not have three number we can push it.
	#     else:
	#         heapq.heappush(min_heap, nums[i])
	#         hash_set.add(nums[i])

	# # 'nums' has only one distinct element it will be the maximum.
	# if len(min_heap) == 1:
	#     return min_heap[0]

	# # 'nums' has two distinct elements.
	# if len(min_heap) == 2:
	#     first_num = min_heap[0]
	#     heapq.heappop(min_heap)
	#     return max(first_num, min_heap[0])

	# return min_heap[0]

    # Time Complexity: O(n)
	# Space Complexity: O(1)

	# maxSet = set()
	# for num in nums:
	# 	maxSet.add(num)
	# 	if len(nums) > 3:
	# 		maxSet.remove(min(maxSet))

	# if len(nums) == 3:
	# 	return min(maxSet)
	# return max(maxSet)

	# Time Complexity: O(n)
	# Space Complexity: O(n)

	# nums = set(nums)
	# if len(nums) < 3:
	# 	return max(nums)
	# return sorted(nums)[-3]

	# Time Complexity: O(nlogn)
	# Space Complexity: O(1)

nums = [3,2,1]
print(thirdMax(nums))

# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.

# Time Complexity:
# Space Complexity: