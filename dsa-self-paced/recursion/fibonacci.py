class Solution:
    def __init__(self, n):
        # As 0th fibonacci number does not exist
        self.fibonacciCache = [None] * (n + 1) 

    def fibonacci(self, n):
        if n == 1 or n == 2:
            return 1
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def fibonacciMemo(self, n):
        if self.fibonacciCache[n]:
            return self.fibonacciCache[n]

        if n == 1:
            fibN = 1
        elif n == 2:
            fibN = 1
        else:
            fibN = self.fibonacciMemo(n - 1) + self.fibonacciMemo(n - 2)
            
        self.fibonacciCache[n] = fibN
        return fibN


if __name__ == "__main__":
    S = Solution(100)
    print(S.fibonacciMemo(100))