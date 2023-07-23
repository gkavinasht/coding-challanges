# 225. Implement Stack using Queues
# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
# Implement the MyStack class:
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:
# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

import collections

class MyStack:
    def __init__(self):
        self.queue1 = collections.deque([])
        self.queue2 = collections.deque([])

    def push(self, x):
        self.queue1.append(x)

    def pop(self):
        self.top()
        return self.queue2.pop()

    def top(self):
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        return self.queue2[-1]

    def empty(self):
        return not self.queue1 and not self.queue2

stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())

# Time Complexity:
# push - O(1), pop - amortized O(1), worst case O(n), peek - amortized O(1), worst case O(n), empty - O(1)
# Space Complexity: O(n)

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False