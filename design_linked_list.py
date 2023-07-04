# 707. Design Linked List
# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:
# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

# Time Complexities:
# Insert - At the beginning - O(1), At a specific position or At the end - O(n)
# Search or Access - At the beginning or specific position or end - O(n)
# Delete - At the beginning or specific position or end - O(n)

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = ListNode()

    def get(self, index: int) -> int:
        curr = self.head.next
        count = 0
        while curr and count != index:
            count += 1
            curr = curr.next
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        prev, curr = self.head, self.head.next
        count = 0
        while curr and count != index:
            count += 1
            prev = curr
            curr = curr.next
        if count == index:
            new_node = ListNode(val)
            new_node.next = curr
            prev.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        prev, curr = self.head, self.head.next
        count = 0
        while curr and count != index:
            count += 1
            prev = curr
            curr = curr.next
        if count == index and curr:
            prev.next = curr.next

obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
print(obj.get(1))
obj.deleteAtIndex(1)
print(obj.get(1))

# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]

# Output
# [null, null, null, null, 2, null, 3]

# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3