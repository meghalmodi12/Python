class StringCompression:
    def __init__(self, data):
        self.data = data
        self.compression = []
        self.counter = 0

    def compress(self):
        for i in range(len(self.data)):
            if i != 0 and self.data[i] != self.data[i - 1]:
                self.compression.append(self.data[i - 1] + str(self.counter))
                self.counter = 0
            self.counter += 1

        self.compression.append(self.data[-1] + str(self.counter))

        # Return minimum of two, key decided the criteria
        return min(self.data, "".join(self.compression), key=len)
                