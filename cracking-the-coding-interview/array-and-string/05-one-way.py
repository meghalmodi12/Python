class IsOneWay:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def oneWayEdit(self):
        edited = None
        s1, s2 = self.str1, self.str2

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if edited is None:
                    edited = True
                else:
                    edited = False
                    break
        
        return True if edited is None else edited

    def oneWayInsert(self):
        '''
        Assuming str1 is shorter
        '''
        edited = None
        i, j = 0, 0
        s1, s2 = self.str1, self.str2

        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                if edited is None:
                    edited = True
                    j += 1
                else:
                    edited = False
                    break
            else:
                i += 1
                j += 1

        return True if edited is None else edited

    def check(self):
        s1, s2 = self.str1, self.str2
        if s1 == s2:
            return True
        elif len(s1) == len(s2):
            return self.oneWayEdit(s1, s2)
        elif len(s1) + 1 = len(s2):
            return self.oneWayInsert(s1, s2)
        elif len(s1) - 1 == len(s2):
            return self.oneWayInsert(s2, s1)
        else:
            return False