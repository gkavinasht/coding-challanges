# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n):
    # Memoization
    # climb_cache = {}

    # def climb(n):
    #     if n <= 1:
    #         return 1

    #     if n in climb_cache:
    #         return climb_cache[n]

    #     total_sum = climb(n - 1) + climb(n - 2)
    #     climb_cache[n] = total_sum

    #     return total_sum
    # return climb(n)

    # Dynamic Programming
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    # Number of ways for 1 and 2 steps
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

n = 3
print(climbStairs(n))

# Time Complexity: O(n)
# Space Complexity: O(n)

# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step