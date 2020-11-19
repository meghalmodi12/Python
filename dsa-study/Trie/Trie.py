from TrieNode import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def getIndex(self, t):
        return ord(t) - ord('a')

    def insert(self, key):
        if key is None:
            return False

        key = key.lower()
        currNode = self.root

        for letter in key:
            index = self.getIndex(letter)

            if currNode.children[index] is None:
                currNode.children[index] = TrieNode(letter)
                print(letter + ' inserted')

            currNode = currNode.children[index]

        currNode.markAsLeaf()
        print(key + ' inserted')

    def search(self, key):
        if key is None:
            return False

        key = key.lower()
        currNode = self.root

        for letter in key:
            index = self.getIndex(letter)

            if currNode.children[index] is None:
                return False
            currNode = currNode.children[index]

        if currNode is not None and currNode.is_end_word:
            return True

        return False

if __name__ == '__main__':
    keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
    output = ["Not present in the trie", "Present in the trie"]

    t = Trie()

    for k in keys:
        t.insert(k)

    if t.search("the") is True:
        print("the --- " + output[1])
    else:
        print("the --- " + output[0])

    if t.search("these") is True:
        print("these --- " + output[1])
    else:
        print("these --- " + output[0])

    if t.search("abc") is True:
        print("abc --- " + output[1])
    else:
        print("abc --- " + output[0])