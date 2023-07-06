# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    slow, fast = head, head

    # Find middle node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    # reverse second half
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # compare first half and second half nodes
    while prev:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next
    return True

first_node = ListNode(1)
second_node = ListNode(2)
third_node = ListNode(2)
fourth_node = ListNode(1)

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
head = first_node

print(isPalindrome(head))

# Time Complexity: O(n)
# Space Complexity: O(1)

# head = [1,2,2,1]
# Output: true