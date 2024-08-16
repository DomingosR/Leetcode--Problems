class Solution(object):
    def maxProduct(self, words):
        n = len(words)
        baseline = ord('a')
        wordMask = defaultdict(int)
        
        for i, word in enumerate(words):
            currentMask = 0
            for indChar in word:
                currentMask |= (1 << (ord(indChar) - baseline))
            wordMask[i] = currentMask
            
        maxProduct = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if (wordMask[i] & wordMask[j] == 0):
                    maxProduct = max(len(words[i]) * len(words[j]), maxProduct)
                    
        return maxProduct