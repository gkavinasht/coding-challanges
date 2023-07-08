# 202. Happy Number
# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

def get_sum_of_squares_of_digits(num):
    sum_of_squares_of_digits = 0
    while num > 0:
        rem = num % 10
        sum_of_squares_of_digits += rem**2
        num //= 10
    return sum_of_squares_of_digits

def isHappy(n):
    if n <= 0:
        return False

    visited = set()
    while n != 1 and n not in visited:
        visited.add(n)
        n = get_sum_of_squares_of_digits(n)

    return n == 1

n = 19
print(isHappy(n))

# Time Complexity: O(logn) depends on the while loop until n becomes 1 or n is in visited
# Space Complexity: O(n)

# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1