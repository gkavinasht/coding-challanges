# 24. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head: ListNode) -> ListNode:
	curr = head
	while curr:
		print(curr.val)
		curr = curr.next

def swapPairs(head: ListNode) -> ListNode:
    # Iterative
    # l3 = ListNode()
    # l3.next = head
    # prev = l3

    # while head and head.next:
    #     first_node = head
    #     second_node = head.next

    #     prev.next = second_node
    #     first_node.next = second_node.next
    #     second_node.next = first_node

    #     prev = first_node
    #     head = first_node.next

    # return l3.next

    # Recursive
    def swap(node):
        if not node or not node.next:
            return node
        
        first_node = node
        second_node = node.next
        
        first_node.next = swap(second_node.next)
        second_node.next = first_node
        
        return second_node
    
    l3 = ListNode()
    l3.next = head
    return swap(l3.next)

# head = [1,2,3,4]

first_node = ListNode(1)
second_node = ListNode(2)
third_node = ListNode(3)
fourth_node = ListNode(4)

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
head = first_node

res_node = swapPairs(head)
printList(res_node)

# Time Complexity: O(n)
# Space Complexity: O(1)

# Output: [2,1,4,3]