# 367. Valid Perfect Square
# Given a positive integer num, return true if num is a perfect square or false otherwise.
# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself. You must not use any built-in library function, such as sqrt.

def isPerfectSquare(num):
    l, r = 1, num

    while l <= r:
        mid = (l + r) // 2
        if mid * mid == num:
            return True
        elif mid * mid < num:
            l = mid + 1
        else:
            r = mid - 1
    return False

num = 16
print(isPerfectSquare(num))

# Time Complexity: O(logn)
# Space Complexity: O(1)

# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.