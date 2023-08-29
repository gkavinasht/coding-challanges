# 46. Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

def permute(nums):
	def backtrack(tempArr):
		if len(tempArr) == n:
			res.append(list(tempArr))
			return

		for i in range(len(nums)):
			if nums[i] not in tempArr:
				tempArr.append(nums[i])
				backtrack(tempArr)
				tempArr.pop()

	n = len(nums)
	res = []
	backtrack([])
	return res

nums = [1,2,3]
print(permute(nums))

# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Time Complexity: O(n * n!)
# Space Complexity: O(n)