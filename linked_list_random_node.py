# 382. Linked List Random Node
# Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.
# Implement the Solution class:
# Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
# int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        scope = 1
        chosen_value = 0
        curr = self.head

        while curr:
            # decide whether to include the element in reservoir
            if random.random() < 1 / scope:
                chosen_value = curr.val
            # move on to the next node
            curr = curr.next
            scope += 1
        return chosen_value

# ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
# [[[1, 2, 3]], [], [], [], [], []]
first_node = ListNode(1)
second_node = ListNode(2)
third_node = ListNode(3)

head = first_node
s = Solution(head)
print(s.getRandom())

# Output
# [null, 1, 3, 2, 2, 3]