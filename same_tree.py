# 100. Same Tree
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode):
    # Iteration
    pstack = collections.deque([p])
    qstack = collections.deque([q])

    while pstack:
        pcurr, qcurr = pstack.popleft(), qstack.popleft()

        if not pcurr and not qcurr:
            continue

        elif not pcurr or not qcurr:
            return False
            
        else:
            if pcurr.val != qcurr.val:
                return False

            pstack.append(pcurr.left)
            pstack.append(pcurr.right)

            qstack.append(qcurr.left)
            qstack.append(qcurr.right)
    
    return True

    # Recursion
    # if p is None and q is None:
    #     return True
    # if p is None or q is None:
    #     return False
    # if p.val != q.val:
    #     return False
    # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# p = [1,2,3]
# q = [1,2,3]

p_first_node = TreeNode(1)
p_second_node = TreeNode(2)
p_third_node = TreeNode(3)

p_first_node.left = p_second_node
p_first_node.right = p_third_node
p = p_first_node

q_first_node = TreeNode(1)
q_second_node = TreeNode(2)
q_third_node = TreeNode(3)

q_first_node.left = q_second_node
q_first_node.right = q_third_node
q = q_first_node

print(isSameTree(p, q))
# Output: true

# Time Complexity: O(n)
# Space Complexity: O(n)