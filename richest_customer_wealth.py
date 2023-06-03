# 1672. Richest Customer Wealth
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the jth bank. Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

def maximumWealth(accounts):
    maximumWealth = 0
    for i in range(len(accounts)):
        wealth = 0
        for j in range(len(accounts[i])):
            wealth += accounts[i][j]
        maximumWealth = max(wealth, maximumWealth)
    return maximumWealth

accounts = [[1,2,3],[3,2,1]]
print(maximumWealth(accounts))

# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.

# Time Complexity : O(m*n)
# Space Complexity : O(1)