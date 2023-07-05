# 142. Linked List Cycle II
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
# Do not modify the linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return curr
            visited.add(curr)
            curr = curr.next
        return None

first_node = ListNode(3)
second_node = ListNode(2)
third_node = ListNode(0)
fourth_node = ListNode(-4)

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = second_node
head = first_node

s = Solution()
res_node = s.detectCycle(head)
print(res_node.val)

# head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Time Complexity : O(n)
# Space Complexity: O(1)