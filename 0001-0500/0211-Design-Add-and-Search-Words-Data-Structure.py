class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
        currentNode.isWord = True

    def search(self, word):
        currentNode = self.root

        def wordMatch(self, auxWord, auxNode):
            if auxWord == "":
                return auxNode.isWord
                
            for char in auxWord:
                if char == ".":
                    for val in auxNode.children:
                        if wordMatch(self, auxWord[1:], auxNode.children[val]):
                            return True
                    return False
                else:
                    if char not in auxNode.children:
                        return False
                    return wordMatch(self, auxWord[1:], auxNode.children[char])
        
        return wordMatch(self, word, self.root)