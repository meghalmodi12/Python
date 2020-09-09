class IsPalindromePermutation:
    def __init__(self, phrase):
        self.phrase = phrase

    def charNum(self, c):
        a, z = ord('a'), ord('z')
        A, Z = ord('A'), ord('Z')
        val = ord(c)

        if a <= val <= z:
            return val - a
        if A <= val <= Z:
            return val - A
        return -1

    def check(self):
        countOdd = 0
        table = [0 for _ in range(ord('z') - ord('a') + 1)]

        for c in self.phrase:
            x = self.charNum(c)
            if x != -1:
                table[x] += 1
                if table[x] % 2 == 0:
                    countOdd -= 1
                else:
                    countOdd += 1

        return countOdd <= 1
        