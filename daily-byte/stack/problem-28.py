"""
Design a class to implement a stack using only a single queue. Your class, QueueStack, should support the following stack methods: push() (adding an item), pop() (removing an item), peek() (returning the top value without removing it), and empty() (whether or not the stack is empty).
"""

from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.myStack = deque()
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def push(self, val):
        self.myStack.append(val)
        self.count += 1

    """
    - Logic is to loop through the queue and append first element we reach count - 1 position
    - Once we reach count - 1 position, we have reached top position so simpley popleft()
    """
    def pop(self):
        if self.count != 0:
            counter = self.count

            while counter - 1 != 0:
                self.myStack.append(self.myStack.popleft())
                counter -= 1

            self.myStack.popleft()
            self.count -= 1

    def peek(self):
        return self.myStack[-1]