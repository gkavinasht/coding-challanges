# 13. Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

def romanToInt(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    result = 0
    curr, next, i = 0, 0, 0
    n = len(s)
    
    while i < n:
        if i == n - 1:
            result += roman[s[i]]
            return result
            
        curr, nex = roman[s[i]], roman[s[i + 1]]
        if curr >= nex:
            result += curr
        else:
            result += (nex - curr)
            i += 1
        i += 1
        
    return result

    # values = {
    #     "I": 1,
    #     "V": 5,
    #     "X": 10,
    #     "L": 50,
    #     "C": 100,
    #     "D": 500,
    #     "M": 1000,
    #     "IV": 4,
    #     "IX": 9,
    #     "XL": 40, 
    #     "XC": 90,
    #     "CD": 400,
    #     "CM": 900
    # }
    # total = 0
    # i = 0
    # while i < len(s):
    #     # This is the subtractive case.
    #     if i < len(s) - 1 and s[i:i+2] in values:
    #         total += values[s[i:i+2]] 
    #         i += 2
    #     else:
    #         total += values[s[i]]
    #         i += 1
    # return total

s = "MCMXCIV"
print(romanToInt(s))

# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Time Complexity: O(n)
# Space Complexity: O(1)