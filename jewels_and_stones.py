# 771. Jewels and Stones
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

def numJewelsInStones(jewels, stones):
    res = 0
    for stone in stones:
        if stone in jewels:
            res += 1
    return res

jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Output: 3