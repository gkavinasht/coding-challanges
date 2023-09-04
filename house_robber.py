# 198. House Robber
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        # Calculate the maximum amount of money if you rob the current house
        # It's the maximum of robbing the current house plus the maximum amount up to two houses back or just skipping the current house and taking the maximum amount up to the previous house.
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    
    return dp[n - 1]
 
nums = [1,2,3,1]
print(rob(nums))

# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Time Complexity: O(n)
# Space Complexity: O(n)