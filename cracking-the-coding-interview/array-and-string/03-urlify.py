class URLify:
    def __init__(self, str1):
        self.str1 = str1

    def replaceSpace(self):
        result = []
        self.str1 = self.str1.strip()

        for c in self.str1:
            if c == ' ':
                result.append('%')
                result.append('2')
                result.append('0')
            else:
                result.append(c)

        return ''.join(result)

        
