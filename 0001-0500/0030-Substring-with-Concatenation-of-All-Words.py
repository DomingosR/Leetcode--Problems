def findSubstringStarts(s, words):
    if not words: 
        return []
    
    subWordLength = len(words[0])
    subWordCount = len(words)
    wordLength = len(s)
    returnVal = []
    
    for left in range(wordLength - subWordLength * subWordCount + 1):
        subWordCounter = collections.Counter(words)
        stillValid = True
        i = 0
        while i < subWordCount and stillValid:
            current = s[left + i * subWordLength:left + (i+1) * subWordLength]
            if subWordCounter.get(current, 0) == 0:
                stillValid = False
            else:
                subWordCounter[current] -= 1
            i += 1
        if stillValid:
            returnVal.append(left)
    
    return returnVal
    
class Solution(object):
    def findSubstring(self, s, words):
        return findSubstringStarts(s, words)