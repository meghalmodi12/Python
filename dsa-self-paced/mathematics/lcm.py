class Solution:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getLCM(self):
        result = max(self.a, self.b)

        while True:
            if self.a % result != 0 and self.b % result != 0:
                break
            else:
                result += 1

        return result