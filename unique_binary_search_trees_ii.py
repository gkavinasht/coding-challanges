# 95. Unique Binary Search Trees II
# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generateTrees(n):
    def allPossibleBST(start, end):
        res = []
        if start > end:
            return [None]

        # Iterate through all values from start to end to construct left, right subtrees recursively.
        for i in range(start, end + 1):
            leftSubTrees = allPossibleBST(start, i - 1)
            rightSubTrees = allPossibleBST(i + 1, end)

            # Loop through all left, right subtrees and connect them to ith root.
            for left in leftSubTrees:
                for right in rightSubTrees:
                    currentTree = TreeNode(i, left, right)
                    res.append(currentTree)
        return res
    return allPossibleBST(1, n) if n else []

n = 3
res = generateTrees(n)
print(res)

# Time Complexity: O(4^n / sqrt(n)) -> total number of possible unique BSTs for n
# Space Complexity: O(4^n / sqrt(n))

# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]