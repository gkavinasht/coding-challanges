# 752. Open the Lock
# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.
# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

import collections
def openLock(deadends, target):
    queue = collections.deque()
    queue.append(("0000", 0))
    visited = set("0000")

    while queue:
        currStr, currSteps = queue.popleft()

        if currStr == target:
            return currSteps

        if currStr in deadends:
            continue

        for i in range(4):
            digit = int(currStr[i])
            for dir in [1, -1]:
                newDigit = (digit + dir) % 10

                newStr = currStr[:i] + str(newDigit) + currStr[i + 1:]
                if newStr not in visited:
                    visited.add(newStr)
                    queue.append((newStr, currSteps + 1))

    return -1

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

print(openLock(deadends, target))

# Time Complexity: O(N^2 * A^N + D) - N: length of the lock (4 in this case), A: number of digits (10 in this case), and D: size of the deadends list.
# Space Complexity: O(A^N + D) - store the visited set and the queue

# Output: 6
# Explanation: 
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".