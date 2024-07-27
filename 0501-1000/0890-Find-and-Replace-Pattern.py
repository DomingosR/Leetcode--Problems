def wordPattern(inputWord):
    auxDict = {}
    pattern = []
    for c in inputWord:
        pattern.append(auxDict.setdefault(c, len(auxDict)))
    return pattern

def matchPattern(words, pattern):
    target = wordPattern(pattern)
    returnVal = []
    for word in words:
        if wordPattern(word) == target:
            returnVal.append(word)
    return returnVal

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return matchPattern(words, pattern)
