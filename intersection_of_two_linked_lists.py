# 160. Intersection of Two Linked Lists
"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
For example, the following two linked lists begin to intersect at node c1:

      a1 -> a2
              -> c1 -> c2 -> c3
b1 -> b2 -> b3

The test cases are generated such that there are no cycles anywhere in the entire linked structure.
Note that the linked lists must retain their original structure after the function returns.
Custom Judge:
The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if headA is None or headB is None:
        return None

    tempA, tempB = headA, headB

    while tempA != tempB:
        tempA = tempA.next
        tempB = tempB.next

        if tempA == tempB:
            return tempA

        if tempA is None:
            tempA = headB
        
        if tempB is None:
            tempB = headA
            
    return tempA

intersectVal = 8
listA = [4,1,8,4,5]
listB = [5,6,1,8,4,5]
skipA = 2
skipB = 3

# Creating Two Linked Lists
first_nodeA = ListNode(4)
second_nodeA = ListNode(1)

first_nodeA.next = second_nodeA

first_nodeB = ListNode(5)
second_nodeB = ListNode(6)
third_nodeB = ListNode(1)

first_nodeB.next = second_nodeB
second_nodeB.next = third_nodeB

common_first_node = ListNode(8)
common_second_node = ListNode(4)
common_third_node = ListNode(5)

common_first_node.next = common_second_node
common_second_node.next = common_third_node

second_nodeA.next = common_first_node
third_nodeB.next = common_first_node

headA = first_nodeA
headB = first_nodeB

res_node = getIntersectionNode(headA, headB)
print(res_node.val)

# Time Complexity: O(n)
# Space Complexity: O(1)

"""
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.
"""