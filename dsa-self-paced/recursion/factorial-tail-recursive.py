class Solution:
    def factorial(self, num, k):
        if num == 0 or num == 1:
            return k
        return self.factorial(num - 1, num * k)

if __name__ == "__main__":
    S = Solution()
    print(S.factorial(5, 1))