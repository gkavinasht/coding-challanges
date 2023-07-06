# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head: ListNode) -> ListNode:
	curr = head
	while curr:
		print(curr.val)
		curr = curr.next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    l3 = ListNode()
    curr = l3
    carry = 0
    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        add = val1 + val2 + carry
        carry = add // 10 
        curr.next = ListNode(add % 10)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        curr = curr.next

    if carry > 0:
        curr.next = ListNode(carry)

    return l3.next

list1_first_node = ListNode(2)
list1_second_node = ListNode(4)
list1_third_node = ListNode(3)

list1_first_node.next = list1_second_node
list1_second_node.next = list1_third_node

list2_first_node = ListNode(5)
list2_second_node = ListNode(6)
list2_third_node = ListNode(4)

list2_first_node.next = list2_second_node
list2_second_node.next = list2_third_node

head1 = list1_first_node
head2 = list2_first_node

res_node = addTwoNumbers(head1, head2)
printList(res_node)

# l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.