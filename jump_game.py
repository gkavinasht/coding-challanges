# 55. Jump Game
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

def canJump(nums):
    n = len(nums)
    if n == 0:
        return False

    # Track farthest index at each position
    dp = [0] * n
    dp[0] = nums[0]

    for i in range(n):
        # Cannot reach the current position
        if i > dp[i - 1]:
            return False

        # Update the farthest index
        dp[i] = max(i + nums[i], dp[i - 1])

        # Can reach the end
        if dp[i] >= n - 1:
            return True

    # Check if the farthest index is at least the last index
    return dp[i] >= n - 1

nums = [2,3,1,1,4]
print(canJump(nums))

# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Time Complexity: O(n)
# Space Complexity: O(n)