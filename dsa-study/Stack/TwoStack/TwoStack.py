class TwoStack:

    def __init__(self, n):
        self.size = n
        self.data = [None] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self, data):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.data[self.top1] = data
        else:
            print("Stack Overflow")
            exit(1)

    def push2(self, data):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.data[self.top2] = data
        else:
            print("Stack Overflow")
            exit(1)

    def pop1(self):
        if self.top1 >= 0:
            answer = self.data[self.top1]
            self.top1 -= 1
            return answer
        else:
            print("Stack Underflow")
            exit(1)

    def pop2(self):
        if self.top2 <= self.size - 1:
            answer = self.data[self.top2]
            self.top2 += 1
            return answer
        else:
            print("Stack Underflow")
            exit(1)