# 1419. Minimum Number of Frogs Croaking
# You are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.
# Return the minimum number of different frogs to finish all the croaks in the given string.
# A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of a valid "croak" return -1.

def minNumberOfFrogs(croakOfFrogs):
    freq = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
    max_frog_croak, present_frog_croak = 0, 0

    for letter in croakOfFrogs:
        if letter == 'c':
            freq['c'] += 1
            present_frog_croak += 1
        elif letter == 'r':
            freq['r'] += 1
        elif letter == 'o':
            freq['o'] += 1
        elif letter == 'a':
            freq['a'] += 1
        elif letter == 'k':
            freq['k'] += 1
            present_frog_croak -= 1

        max_frog_croak = max(max_frog_croak, present_frog_croak)

        if freq['c'] < freq['r'] or freq['r'] < freq['o'] or freq['o'] < freq['a'] or freq['a'] < freq['k']:
            return -1 

    if present_frog_croak == 0 and len(list(set(freq.values()))) == 1:
        return max_frog_croak
    return -1

croakOfFrogs = "croakcroak"
print(minNumberOfFrogs(croakOfFrogs))

# Output: 1 
# Explanation: One frog yelling "croak" twice.

# Time Complexity: O(n)
# Space Complexity: O(1)