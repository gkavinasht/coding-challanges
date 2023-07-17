# 739. Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

def dailyTemperatures(self, T: List[int]) -> List[int]:
    stack = []
    ans = [0] * len(T)

    for i in range(len(T) - 1, -1, -1):
        while stack and T[i] >= T[stack[-1]]:
            stack.pop()
        if stack:
            ans[i] = stack[-1] - i
        stack.append(i)
    return ans

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))

# Time Complexity: O(n)
# Space Complexity: O(n)
# Output: [1,1,4,2,1,1,0,0]