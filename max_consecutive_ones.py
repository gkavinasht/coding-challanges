# 485. Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

def findMaxConsecutiveOnes(nums):
    maxFrequency = frequency = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            frequency += 1
        else:
            maxFrequency = max(frequency, maxFrequency)
            frequency = 0
    maxFrequency = max(frequency, maxFrequency)
    return maxFrequency

nums = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))

# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Time Complexity : O(n)
# Space Complexity: O(1)