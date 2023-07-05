# 203. Remove Linked List Elements
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head: ListNode) -> ListNode:
	curr = head
	while curr:
		print(curr.val)
		curr = curr.next

def removeElements(head: ListNode, val: int) -> ListNode:
    dummy = ListNode(None)
    dummy.next = head
    prev, curr = dummy, head
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummy.next

first_node = ListNode(1)
second_node = ListNode(2)
third_node = ListNode(6)
fourth_node = ListNode(3)
fifth_node = ListNode(4)
sixth_node = ListNode(5)
seventh_node = ListNode(6)

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fifth_node
fifth_node.next = sixth_node
sixth_node.next = seventh_node
head = first_node
val = 6

res_node = removeElements(head, val)
printList(head)

# Time Complexity: O(n)
# Space Complexity: O(1)

# head = [1,2,6,3,4,5,6]
# Output: [1,2,3,4,5]