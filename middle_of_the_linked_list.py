# 876. Middle of the Linked List

# Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.

class ListNode:
	def __init__(self, val=0, next=None):
	    self.val = val
	    self.next = next

	def create(self, l):
	    lst = self
	    prev = lst
	    for i in l:
	        prev.next = ListNode(i)
	        prev = prev.next
	    return lst.next

	def printlst(self, l):
	    curr = l
	    while curr:
	        print(curr.val)
	        curr = curr.next

class Solution:
    def middleNode(self, head):
        current = head
        length = 0
        while current:
            length += 1 
            current = current.next

        middlePosition = (length // 2) + 1

        current = head
        currentPosition = 0
        while current:
            currentPosition += 1
            if currentPosition == middlePosition:
                return current
            current = current.next

        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow


lst1 = [1,2,3,4,5]
l = ListNode()
l1 = l.create(lst1)

s = Solution()
l2 = s.middleNode(l1)
l.printlst(l2)

# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Time Complexity : O(n)
# Space Complexity : O(1)