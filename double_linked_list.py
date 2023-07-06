# Double Linked List
"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
"""

class ListNode:
	def __init__(self, val=None, prev=None, next=None):
		self.val = val
		self.prev = prev
		self.next = next

class LinkedList:
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
        new_node.prev = self.head
        new_node.next = self.head.next
        if self.head.next:
            self.head.next.prev = new_node
        self.head.next = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        curr = self.head.next
        while curr and curr.next:
            curr = curr.next
        if curr:
            curr.next = new_node
        else:
            self.head.next = new_node
        new_node.prev = curr

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        count = 0
        curr = self.head.next
        while curr:
            if count == index:
                temp = curr.prev
                temp.next = new_node
                new_node.prev = temp
                new_node.next = curr
                break
            count += 1
            curr = curr.next
        if not curr and count == index:  # Add at tail
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        count = 0
        curr = self.head.next
        while curr:
            if count == index:
                temp = curr.prev
                temp.next = curr.next
                if curr.next:
                    curr.next.prev = temp
                break
            count += 1
            curr = curr.next

obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
# obj.addAtIndex(1,2)
print(obj.get(1))
obj.deleteAtIndex(1)
print(obj.get(1))

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