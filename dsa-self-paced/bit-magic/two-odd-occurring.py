class Solution:
    def __init__(self, nums):
        self.nums = nums
        
    def getTwoOddOccurringNumbers(self):
        xor = 0
        nums = self.nums

        for num in nums:
            xor = xor ^ num

        # Get the rightmost set bit,
        # that also represtents one of the two odd occurring numbers
        numT = xor & ~(xor - 1)
        num1, num2 = 0, 0

        for num in nums:
            if num & numT != 0:
                num1 = num1 ^ num
            else:
                num2 = num2 ^ num

        return [num1, num2]

if __name__ == "__main__":
    S = Solution([1, 1, 2, 3, 3, 3, 3, 4, 5, 5])
    print(S.getTwoOddOccurringNumbers())

        
