# 1051. Height Checker
# A school is trying to take an annual photo of all the students. 
# The students are asked to stand in a single file line in non-decreasing order by height. 
# Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
# You are given an integer array heights representing the current order that the students are standing in. 
# Each heights[i] is the height of the ith student in line (0-indexed).
# Return the number of indices where heights[i] != expected[i].

def heightChecker(heights):
    # Using Counting Sort
    max_ele = max(heights)
    heights_count = [0] * (max_ele + 1)
    expected = [0] * len(heights)

    # Count the frequencies of each height in the heights array
    for height in heights:
        heights_count[height] += 1

    # Modify the heights_count array to store the cumulative count of each element. This step helps determine the correct positions of elements in the sorted output array.
    for i in range(1, len(heights_count)):
        heights_count[i] += heights_count[i - 1]

    # Generate the expected array based on the height frequencies
    for height in reversed(heights):
        expected[heights_count[height] - 1] = height
        heights_count[height] -= 1

    # Time Complexity: O(n + k)
    # Space Complexity: O(n + k)

    # expected = sorted(heights)

    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)

    unmatched_indices = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            unmatched_indices += 1
    return unmatched_indices

heights = [1,1,4,2,1,3]
print(heightChecker(heights))

# Output: 3
# Explanation: 
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.