# 50. Pow(x, n)
# Implement pow(x, n), which calculates x raised to the power n (i.e., x**n).

def myPow(x, n):
    if n == 0:
        return 1

    if n < 0:
        n = -1 * n
        x = 1.0 / x

    result = 1
    while n != 0:
        # If 'n' is odd we multiply result with 'x' and reduce 'n' by '1'.
        if n % 2 == 1:
            result *= x
            n -= 1
        # We square 'x' and reduce 'n' by half, x^n => (x^2)^(n/2).
        x *= x
        n //= 2
    return result

x = 2.00000
n = 10
print(myPow(x, n))

# Time Complexity: O(logn)
# Space Complexity: O(1)

# Output: 1024.00000