class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.numWordsBelow = 0
        self.word = ""
    
    # To add a word, enter each character as a key in a dictionary in its parent (previous letter),
    # and update count along each node of the path.  Mark the last node as the ending to a word
    def addWord(self, word):
        currentNode = self
        currentNode.numWordsBelow += 1
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
            currentNode.numWordsBelow += 1
        currentNode.isWord = True
        currentNode.word = word
    
    # To remove a word, simply reduce the word count along the trie path by one,
    # and mark the final node as not a word
    def removeWord(self, word):
        currentNode = self
        currentNode.numWordsBelow -= 1
        for char in word:
            if char in currentNode.children:
                currentNode = currentNode.children[char]
                currentNode.numWordsBelow -= 1
        currentNode.isWord = False
        currentNode.word = ""

class Solution(object):
    def findWords(self, board, words):
        # First, build word trie and add words to it
        trieRoot = TrieNode()
        for word in words:
            trieRoot.addWord(word)

        # Parameters to main procedure
        numRows, numCols = len(board), len(board[0])
        foundWords = set()
        visitedCells = set()

        def dfs(i, j, currentNode):
            # First, check if we can continue with this cell, and add
            # character to word and navigate through trie if so
            if (i < 0 or i == numRows or j < 0 or j == numCols
                or board[i][j] not in currentNode.children
                or currentNode.children[board[i][j]].numWordsBelow < 1
                or (i, j) in visitedCells
                ):
                return

            currentChar = board[i][j]
            visitedCells.add((i, j))
            currentNode = currentNode.children[currentChar]

            # Check if current trie node is a word, and add it to foundWords 
            # if that's the case
            if currentNode.isWord:
                currentWord = currentNode.word
                foundWords.add(currentWord)
                trieRoot.removeWord(currentWord)

            # Then proceed to the other nodes in adjacent cells
            dfs(i + 1, j, currentNode)
            dfs(i - 1, j, currentNode)
            dfs(i, j + 1, currentNode)
            dfs(i, j - 1, currentNode)

            # Once done processing neighboring cells, mark this node as not visited
            # before moving one level up in recursions
            visitedCells.remove((i, j))

        for i in range(numRows):
            for j in range(numCols):
                dfs(i, j, trieRoot)
        
        return list(foundWords)