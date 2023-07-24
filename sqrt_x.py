# 69. Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

def mySqrt(x):
    if x == 0 or x == 1:
        return x

    l, r = 0, x
    while l <= r:
        mid = (l + r) // 2

        if mid > x / mid:
            r = mid - 1
        elif mid < x / mid:
            l = mid + 1
        else:
            return mid
    # The integer square root will be in the right variable
    return r

x = 4
print(mySqrt(x))

# Time Complexity: O(logn)
# Space Complexity: O(1)

# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.