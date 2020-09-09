class Queue:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.data = [None] * Queue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0

    def _len(self):
        return self.size

    def isEmpty(self):
        return self._len() == 0

    def first(self):
        if self.isEmpty():
            raise("Queue is empty")
        return self.data[self.front]

    def enqueue(self, data):
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        available = (self.front + self.size) % len(self.data)
        self.data[available] = data
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise("Queue is empty")
        answer = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1

        if 0 < self.size < len(self.data) // 4:
            self.resize(len(self.data) // 2)

        return answer

    def resize(self, newSize):
        oldQueue = self.data
        self.data = [None] * newSize

        walk = self.front
        for k in range(self.size):
            self.data[k] = oldQueue[walk]
            walk = (1 + walk) % len(oldQueue)
        self.front = 0
