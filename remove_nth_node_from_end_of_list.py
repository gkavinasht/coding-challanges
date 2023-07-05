# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(None)
    dummy.next = head
    curr = head
    length = 0

    while curr:
        length += 1
        curr = curr.next

    del_position = length - n
    index = 0
    prev, curr = dummy, head

    while curr:
        if index == del_position:
            prev.next = curr.next
            break
        index += 1
        prev = curr
        curr = curr.next
    
    return dummy.next

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

n = 2
res_node = removeNthFromEnd(head, n)
print(f"{res_node.val} {res_node.next.val} {res_node.next.next.val} {res_node.next.next.next.val}")


# Time Complexity : O(n)
# Space Complexity: O(1)

# Output: [1,2,3,5]