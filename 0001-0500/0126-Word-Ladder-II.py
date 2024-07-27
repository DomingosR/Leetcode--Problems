from collections import defaultdict, Counter

def validPaths(originalWord, listWords, targetWord):
    # First, handle the trivial case
    listWords = set(listWords)
    if targetWord not in listWords:
        return []

    # Breadth-first recursion    
    currentLevel = {originalWord}
    parentWords = defaultdict(list)
    while currentLevel:
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
            break

        currentLevel = nextLevel
    
    # Reconstruction of minimum-length paths
    returnVal = []
    
    def dfs(word, path):
        if word == originalWord:
            path.append(word)
            returnVal.append(path[::-1])
        else:
            for parentWord in parentWords[word]:
                dfs(parentWord, path + [word])
    
    dfs(targetWord, [])
    
    return returnVal

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        return validPaths(beginWord, wordList, endWord)