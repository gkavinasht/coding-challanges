# 45. Jump Game II
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

def jump(nums):
    n = len(nums)
    if n == 1:
        return 0

    jumps = 0
    # Boundary of the current jump
    curr_jump_end = 0

    # Track farthest index at each position
    dp = [0] * n
    for i in range(n):
        # Update the farthest index
        dp[i] = max(dp[i - 1], i + nums[i])

        # forced to jump (by lazy jump) to extend coverage
        if i == curr_jump_end:
            # update last jump index
            curr_jump_end = dp[i]
            # As the boundary of the current jump is reached, make a new jump
            jumps += 1

            # check if destination can be reached
            if dp[i] >= n - 1:
                return jumps
    return jumps

nums = [2,3,1,1,4]
print(jump(nums))

# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Time Complexity: O(n)
# Space Complexity: O(n)