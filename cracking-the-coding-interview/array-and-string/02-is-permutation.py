class IsPermutation:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.charDict = {}

    def check(self):
        for letter in self.str1:
            if letter not in self.charDict:
                self.charDict[letter] = 0
            self.charDict[letter] += 1

        for letter in self.str2:
            if letter in self.charDict:
                self.charDict[letter] -= 1
                if self.charDict[letter] == 0:
                    del self.charDict[letter]
            else:
                return False

        return len(self.charDict.keys()) == 0
