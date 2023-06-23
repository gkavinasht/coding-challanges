# 747. Largest Number At Least Twice of Others
# You are given an integer array nums where the largest integer is unique.
# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

import heapq

def dominantIndex(nums):
	first_max = -1
	second_max = -1
	index = -1
	for i in range(len(nums)):
	    if nums[i] > first_max:
	        second_max = first_max
	        first_max = nums[i]
	        index = i 
	    elif nums[i] > second_max:
	        second_max = nums[i]

	if first_max >= 2 * second_max:
	    return index
	return -1

    # Time Complexity: O(n)
	# Space Complexity: O(1)

	# min_heap = []
	# index_dict = {}

	# for i in range(len(nums)):
	#     if len(min_heap) == 2:
	#         if nums[i] > min_heap[0]:
	#             heapq.heappop(min_heap)
	#             heapq.heappush(min_heap, nums[i])
	#             index_dict[nums[i]] = i
	#     else:
	#         heapq.heappush(min_heap, nums[i])
	#         index_dict[nums[i]] = i

	# if len(min_heap) == 2:
	#     second_max = min_heap[0]
	#     heapq.heappop(min_heap)
	#     if 2 * second_max <= min_heap[0]:
	#         return index_dict[min_heap[0]]
	# return -1

    # Time Complexity: O(nlogk) --> logk to perform heappush and heappop operations
	# Space Complexity: O(n)

	# for i in range(len(nums)):
	#     match = 0
	#     for j in range(len(nums)):
	#         if i != j:
	#             if nums[i] < 2 * nums[j]:
	#                 break
	#             else:
	#                 match += 1
	#     if match == len(nums) - 1:
	#         return i
	# return -1

	# Time Complexity: O(n*2)
	# Space Complexity: O(1)

nums = [3,6,1,0]
print(dominantIndex(nums))

# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.