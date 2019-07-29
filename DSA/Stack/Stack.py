class Stack:

    def __init__(self):
        self.data = []
    
    def size(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, element):
        self.data.append(element)

    # Also known as peek
    def top(self):
        if self.isEmpty():
            raise("Stack is empty")
        return self.data[-1]

    def pop(self):
        if self.isEmpty():
            raise("Stack is empty")
        return self.data.pop()

    