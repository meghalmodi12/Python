class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        uniqueChars = []
        uniqueCharsDict = {}
        
        for i in range(len(s)):
            uniqueChars.append(s[i])
            if s[i] not in uniqueCharsDict:
                uniqueCharsDict[s[i]] = 0
            uniqueCharsDict[s[i]] += 1
            
            while len(uniqueChars) > len(uniqueCharsDict.keys()):
                char = uniqueChars.pop(0)
                if uniqueCharsDict[char] == 1:
                    del uniqueCharsDict[char]
                else:
                    uniqueCharsDict[char] -= 1
                
            result = max(result, len(uniqueChars))
            
        return result