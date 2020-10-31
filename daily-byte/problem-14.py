"""
This question is asked by Amazon. Given two strings representing sentences, return the words that are not common to both strings (i.e. the words that only appear in one of the sentences). You may assume that each sentence is a sequence of words (without punctuation) correctly separated using space characters.

Ex: given the following strings...

sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", return ["beat", "to", "lost"]
sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]
"""

def uncommonWords(sentence1, sentence2):
    wordDict = {}
    result = []
    
    for word in sentence1.split(" "):
        if word in wordDict:
            wordDict[word] = -1
        else:
            wordDict[word] = 1
            
    for word in sentence2.split(" "):
        if word in wordDict:
            wordDict[word] = -1
        else:
            wordDict[word] = 1
            
    for key, value in wordDict.items():
        if value == 1:
            result.append(key)
                    
    return result

print(uncommonWords('the quick', 'brown fox'))
print(uncommonWords('the tortoise beat the haire', 'the tortoise lost to the haire'))
print(uncommonWords('copper coffee pot', 'hot coffee pot'))