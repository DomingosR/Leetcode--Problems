class Trie(object):
    def __init__(self):
        self.children = {}
        self.isWord = False

    def insert(self, word):
        currentNode = self
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = Trie()
            currentNode = currentNode.children[char]
        currentNode.isWord = True
        
    def search(self, word):
        currentNode = self
        for char in word:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
        return currentNode.isWord

    def startsWith(self, prefix):
        currentNode = self
        for char in prefix:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
        return True