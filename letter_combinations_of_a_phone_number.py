# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

def letterCombinations(digits):
    phone = {
        '2' : ['a', 'b', 'c'],
        '3' : ['d', 'e', 'f'],
        '4' : ['g', 'h', 'i'],
        '5' : ['j', 'k', 'l'],
        '6' : ['m', 'n', 'o'],
        '7' : ['p', 'q', 'r', 's'],
        '8' : ['t', 'u', 'v'],
        '9' : ['w', 'x', 'y', 'z']
    }

    def backtrack(comb, digits):
    	if len(digits) == 0:
    		res.append(comb)
    		return

    	for letter in phone[digits[0]]:
    		comb += letter
    		backtrack(comb, digits[1:])
    		comb = comb[:-1]

    res = []
    if digits:
    	backtrack("", digits)
    return res

digits = "23"
print(letterCombinations(digits))

# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Time Complexity: O(4^n)
# Space Complexity: O(n + 4^n)