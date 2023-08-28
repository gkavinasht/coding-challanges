# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

def combine(n, k):
    def backtrack(comb = [], first = 1):
        if len(comb) == k:
            res.append(list(comb))
            return

        for i in range(first, n + 1):
            comb.append(i)
            backtrack(comb, i + 1)
            comb.pop()
    res = []
    backtrack()
    return res

n = 4
k = 2
print(combine(n, k))

# Time Compelxity: O(C(n, k))
# Space Complexity: O(C(n, k)) + Recursive stack calls

# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.