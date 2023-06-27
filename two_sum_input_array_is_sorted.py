# 167. Two Sum II - Input array is sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

def twoSum(numbers, target):
	l, r = 0, len(numbers) - 1
	while l < r:
	    s = numbers[l] + numbers[r]
	    if s == target:
	        return [l + 1, r + 1]
	    elif s < target:
	        l += 1
	    else:
	        r -= 1
	return []

	# Time Complexity: O(n)
    # Space Complexity: O(1)

    # numbers_dict = {}
    # for i in range(len(numbers)):
    #     rem = target - numbers[i]
    #     if rem in numbers_dict:
    #         return [numbers_dict[rem], i + 1]
    #     numbers_dict[numbers[i]] = i + 1
    # return []

    # Time Complexity: O(n)
    # Space Complexity: O(n)

numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))

# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].