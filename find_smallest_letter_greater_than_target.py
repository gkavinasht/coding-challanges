# 744. Find Smallest Letter Greater Than Target
# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

def nextGreatestLetter(letters, target):
    # for ch in letters:
    #     if ch > target:
    #         return ch

    # return letters[0]

    l, r = 0, len(letters) - 1
    while l <= r:
        mid = (l + r) // 2

        if letters[mid] > target:
            r = mid - 1
        elif letters[mid] <= target:
            l = mid + 1

    return letters[0] if l == len(letters) else letters[l]

letters = ["c","f","j"]
target = "a"

print(nextGreatestLetter(letters, target))

# Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.