# 494. Target Sum
# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

class Solution:
    # DP or Memoization
    def __init__(self):
        self.memo = {}

    def calculate(self, nums, index, target):
        if index == len(nums):
            return 1 if target == 0 else 0

        if (index, target) in self.memo:
            return self.memo[(index, target)]

        # Calculate the number of ways with '+' and '-' symbols for the current number
        add = self.calculate(nums, index + 1, target + nums[index])
        subtract = self.calculate(nums, index + 1, target - nums[index])
        ways = add + subtract

        # Store the result in memo to avoid redundant calculations
        self.memo[(index, target)] = ways
        return ways

    def findTargetSumWays(self, nums, target):
        return self.calculate(nums, 0, target)

    # Time Complexity: O(n*s) -> n: number of elements, s: sum of all the elements
    # Space Complexity: O(n*s) -> memo

    # Brute Force
    # def __init__(self):
    #     self.count = 0

    # def calculate(self, nums, index, target):
    #     if index == len(nums):
    #         if target == 0:
    #             self.count += 1
    #     else:
    #         self.calculate(nums, index + 1, target + nums[index])
    #         self.calculate(nums, index + 1, target - nums[index])

    # def findTargetSumWays(self, nums, target):
    #     self.calculate(nums, 0, target)
    #     return self.count

    # Time Complexity: O(2**n)
    # Space Complexity: O(n)

s = Solution()

nums = [1,1,1,1,1]
target = 3
print(s.findTargetSumWays(nums, target))

# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3