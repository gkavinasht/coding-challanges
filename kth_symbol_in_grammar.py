# 779. K-th Symbol in Grammar
# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

def kthGrammar(n, k):
    # Optimized
    if n == 1:
        return 0

    # Number of digits gets doubled for each row
    mid = (2 ** (n - 1)) // 2
    if k <= mid:
        return kthGrammar(n - 1, k)
    else:
        return 1 if kthGrammar(n - 1, k - mid) == 0 else 0

    # Time Complexity: O(n)
    # Space Complexity: O(logn)

    # Finding nth row and get the kth index
    # def nthRow(n):
    #     if n == 1:
    #         return "0"

    #     previousRow = nthRow(n - 1)
    #     nth_row = ""

    #     for ch in previousRow:
    #         if ch == "0":
    #             nth_row += "01"
    #         else:
    #             nth_row += "10"

    #     return nth_row

    # return int(nthRow(n)[k - 1])

    # Time Complexity: O(2^n)
    # Space Complexity: O(n*2^n)

n = 2
k = 1
print(kthGrammar(n, k))

# Output: 0
# Explanation: 
# row 1: 0
# row 2: 01