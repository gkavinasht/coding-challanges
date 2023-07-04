# 141. Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

first_node = ListNode(3)
second_node = ListNode(2)
third_node = ListNode(0)
fourth_node = ListNode(-4)

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = first_node
head = first_node

s = Solution()
print(s.hasCycle(head))

# head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Time Complexity : O(n)
# Space Complexity: O(1)