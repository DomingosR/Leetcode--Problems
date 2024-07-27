from collections import defaultdict, Counter

def minimumLengthOfValidPaths(originalWord, listWords, targetWord):
    # First, handle the trivial case
    listWords = set(listWords)
    if targetWord not in listWords:
        return 0

    # Breadth-first recursion    
    currentLevel = {originalWord}
    numLevels = 1
    parentWords = defaultdict(list)
    
    while currentLevel:
        numLevels += 1
        listWords -= currentLevel
        nextLevel = set()
        
        for word in currentLevel:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in listWords:
                        nextLevel.add(newWord)
                        parentWords[newWord].append(word)
        if targetWord in nextLevel:
            return numLevels

        currentLevel = nextLevel
    
    return 0


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return minimumLengthOfValidPaths(beginWord, wordList, endWord)