# 42. Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

def trap(height):
    length = len(height)
    if length == 0:
        return 0
    
    totalWater = 0
    leftMax = [0]*length
    rightMax = [0]*length
    
    leftMax[0] = height[0]
    for i in range(1,length):
        leftMax[i] = max(height[i], leftMax[i-1])
        
    rightMax[length-1] = height[length-1]
    for i in range(length-2,-1,-1):
        rightMax[i] = max(height[i], rightMax[i+1])
        
    for i in range(length):
        totalWater += min(leftMax[i], rightMax[i]) - height[i]
        
    return totalWater

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))

# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Time Complexity: O(n)
# Space Complexity: O(n)