# 92. Reverse Linked List II
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head: ListNode) -> ListNode:
	curr = head
	while curr:
		print(curr.val)
		curr = curr.next

def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    prev, curr = None, head
    index = 0

    while curr and index < m - 1:
        index += 1
        prev = curr
        curr = curr.next

    start, end = prev, curr

    while curr and index < n:
        index += 1
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    if start:
        start.next = prev
    else:
        head = prev
    end.next = curr

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

left = 2
right = 4

res_node = reverseBetween(head, left, right)
printList(res_node)

# Time Complexity: O(n)
# Space Complexity: O(1)

# head = [1,2,3,4,5]
# Output: [1,4,3,2,5]