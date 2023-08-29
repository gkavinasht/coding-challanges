# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

def generateParenthesis(n):
	res = []
	stack = []

	def backtrack(openN, closedN):
		if openN == closedN == n:
			res.append("".join(stack))
			return

		if openN < n:
			stack.append("(")
			backtrack(openN + 1, closedN)
			stack.pop()

		if closedN < openN:
			stack.append(")")
			backtrack(openN, closedN + 1)
			stack.pop()

	backtrack(0, 0)
	return res

n = 3
print(generateParenthesis(n))
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Time Complexity: O(2^(2 * n)) -> maximum length of string 2 * n, two choices at each location
# Space Complexity: O(n) -> stack, recursion call stack
