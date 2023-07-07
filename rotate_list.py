# 61. Rotate List
# Given the head of a linked list, rotate the list to the right by k places.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head: ListNode) -> ListNode:
	curr = head
	while curr:
		print(curr.val)
		curr = curr.next

def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head or not head.next:
        return head

    # Link last node with first node creating cycle
    length = 1
    old_tail = head
    while old_tail.next:
        length += 1
        old_tail = old_tail.next
    old_tail.next = head

    # Create new_tail and new_head
    curr, new_tail = head, head
    count = 0
    while curr:
        if count == length - k % length - 1:
            break
        count += 1
        new_tail = new_tail.next
        curr = curr.next
    new_head = new_tail.next

    # Cut link between new_tail and new_head
    new_tail.next = None

    return new_head

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
k = 2

res_node = rotateRight(head, k)
printList(res_node)

# Time Complexity: O(n)
#Space Complexity: O(1)

# head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
