# 430. Flatten a Multilevel Doubly Linked List
# You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.
# Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.
# Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def printList(head: Node) -> Node:
	curr = head
	while curr:
		print(curr.val)
		curr = curr.next

def flatten(head: Node) -> Node:
    if head is None:
        return head

    curr = head
    while curr:
        # If no child exists
        if curr.child is None:
            curr = curr.next
            continue

        # If there is child, find tail of the child and link it to curr.next
        temp = curr.child
        # Find tail of the child
        while temp.next:
            temp = temp.next
        # Connext tail with curr.next, if not None
        temp.next = curr.next
        if curr.next:
            curr.next.prev = temp

        # Connect curr with curr.child and remove curr.child
        curr.next = curr.child
        curr.child.prev = curr
        curr.child = None
    return head

    # Time Complexity: O(n)
    # Space Complexity: O(1)

    # if not head:
    #     return head
    
    # pseudoHead = Node(None, None, head, None)
    # prev = pseudoHead
    
    # stack = []
    # stack.append(head)
    
    # while stack:
    #     curr = stack.pop()
        
    #     prev.next = curr
    #     curr.prev = prev
        
    #     if curr.next:
    #         stack.append(curr.next)
            
    #     if curr.child:
    #         stack.append(curr.child)
    #         curr.child = None
            
    #     prev = curr
        
    # pseudoHead.next.prev = None
    # return pseudoHead.next

    # Time Complexity: O(n)
    # Space Complexity: O(n)


first_node = Node(1)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)
fifth_node = Node(5)
sixth_node = Node(6)
seventh_node = Node(7)
eighth_node = Node(8)
ninth_node = Node(9)
tenth_node = Node(10)

first_node.next = second_node
second_node.prev = first_node
second_node.next = third_node
third_node.prev = second_node
third_node.next = fourth_node
third_node.child = fifth_node
fourth_node.prev = third_node
fifth_node.next = sixth_node
sixth_node.prev = fifth_node
sixth_node.next = seventh_node
sixth_node.child = ninth_node
seventh_node.prev = sixth_node
seventh_node.next = eighth_node
eighth_node.prev = seventh_node
ninth_node.next = tenth_node
tenth_node.prev = ninth_node

head = first_node
res_node = flatten(head)
print("Flatten List:")
printList(res_node)

# 1 -> 2 -> 3 -> 4
#           |
#           5 -> 6 -> 7 -> 8
#           	 |
#           	 9 -> 10
# head = [1,2,3,4,null,5,6,7,null,8,9]
# Output: [1,2,3,5,6,9,10,7,8,4]
# Explanation: The multilevel linked list in the input is shown.
# After flattening the multilevel linked list it becomes:
# 1 -> 2 -> 3 -> 5 -> 6 -> 9 -> 10 -> 7 -> 8 -> 4