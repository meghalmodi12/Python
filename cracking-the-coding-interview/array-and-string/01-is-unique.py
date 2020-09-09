class IsUnique:
    def __init__(self, value):
        self.value = value
        self.charCount = {}

    def check(self):
        for letter in self.value:
            if letter not in self.charCount:
                self.charCount[letter] = 0
            self.charCount[letter] += 1

        return len(self.value) == len(self.charCount.keys())