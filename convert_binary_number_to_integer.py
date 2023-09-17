# 1290. Convert Binary Number in a Linked List to Integer
# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.
# The most significant bit is at the head of the linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head: ListNode):
    length = 0
    curr = head

    while curr:
        length += 1
        curr = curr.next

    curr = head
    res = 0
    while curr:
        length -= 1
        res += curr.val * (2**length)
        curr = curr.next

    return res

# head = [1,0,1]
first_node = ListNode(1)
second_node = ListNode(0)
third_node = ListNode(1)

first_node.next = second_node
second_node.next = third_node
head = first_node
print(getDecimalValue(head))

# Output: 5
# Explanation: (101) in base 2 = (5) in base 10

# Time Complexity: O(n)
# Space Complexity: O(1)