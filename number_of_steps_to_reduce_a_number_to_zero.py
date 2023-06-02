# 1342. Number of Steps to Reduce a Number to Zero

# Given an integer num, return the number of steps to reduce it to zero. In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

def numberOfSteps(self, num: int) -> int:
    # Time Complexity : O(logn)
    # Space Complexity : O(1)
    numberOfSteps = 0
    while num > 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        numberOfSteps += 1
    return numberOfSteps

    # Bitwise Operator
    # Time Complexity : O(logn)
    # Space Complexity : O(1)
    # numberOfSteps = 0
    # while num > 0:
    #     if num & 1 == 0: # Using Bitmask 00000001
    #         num >>= 1 # Shifting each bit to right, divides the number into half
    #     else:
    #         num -= 1
    #     numberOfSteps += 1
    # return numberOfSteps


# Output: 6
# Explanation: 
# Step 1) 14 is even; divide by 2 and obtain 7. 
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3. 
# Step 4) 3 is odd; subtract 1 and obtain 2. 
# Step 5) 2 is even; divide by 2 and obtain 1. 
# Step 6) 1 is odd; subtract 1 and obtain 0.