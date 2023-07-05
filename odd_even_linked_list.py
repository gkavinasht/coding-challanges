# 328. Odd Even Linked List
# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head: ListNode) -> ListNode:
	curr = head
	while curr:
		print(curr.val)
		curr = curr.next

def oddEvenList(head: ListNode) -> ListNode:
    if head is None:
        return None

    odd, even = head, head.next
    evenHead = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = evenHead
    return head

first_node = ListNode(1)
second_node = ListNode(2)
third_node = ListNode(3)
fourth_node = ListNode(4)
fifth_node = ListNode(5)

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fifth_node
head = first_node

res_node = oddEvenList(head)
printList(head)

# Time Complexity: O(n)
# Space Complexity: O(1)

# head = [1,2,3,4,5]
# Output: [1,3,5,2,4]