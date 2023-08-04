# 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head: ListNode) -> ListNode:
	curr = head
	while curr:
		print(curr.val)
		curr = curr.next

def reverseList(head: ListNode) -> ListNode:
    # Iteration
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

    # Time Complexity : O(n)
    # Space Complexity: O(1)

    # Recursion
    # def reverse(prev, curr):
    #     if not curr:
    #         return prev

    #     temp = curr.next
    #     curr.next = prev
    #     return reverse(curr, temp)

    # return reverse(None, head)

    # Time Complexity : O(n)
    # Space Complexity: O(n)

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

res_node = reverseList(head)
printList(res_node)

# head = [1,2,3,4,5]
# Output: [5,4,3,2,1]