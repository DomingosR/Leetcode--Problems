class Solution(object):
    def printVertically(self, s):
        words = s.split()
        numWords = len(words)
        
        maxRemainingLen = [0] * numWords
        maxRemainingLen[-1] = len(words[-1])
        
        for i in range(numWords - 2, -1, -1):
            maxRemainingLen[i] = max(maxRemainingLen[i+1], len(words[i]))
            
        transposedWords = []
        
        for j in range(maxRemainingLen[0]):
            currentWord, k = "", 0
            while k < numWords and maxRemainingLen[k] >= j+1:
                if len(words[k]) >= j+1:
                    currentWord += words[k][j]
                else:
                    currentWord += " "
                k += 1
            transposedWords.append(currentWord)
            
        return transposedWords