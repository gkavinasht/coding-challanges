# 509. Fibonacci Number
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

def fib(N):
	# Recursion with Memoization
    fib_cache = {}

    def fibSum(n):
        if n <= 1:
            return n

        if n in fib_cache:
            return fib_cache[n]

        totalSum = fibSum(n - 1) + fibSum(n - 2)
        fib_cache[n] = totalSum

        return totalSum
    return fibSum(N)

n = 3
return(fib(n))

# Time Complexity: O(n) -> Due to Memoization, without it - 2**n
# Space Complexity: O(n)

# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.