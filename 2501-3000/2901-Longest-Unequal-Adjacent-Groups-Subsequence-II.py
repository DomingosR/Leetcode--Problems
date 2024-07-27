class Solution(object):
    def getWordsInLongestSubsequence(self, words, groups):
        def follows(i, j):
            if groups[j] == groups[i] or len(words[j]) != len(words[i]):
                return False
            if len([k for k in range(len(words[i])) if words[i][k] != words[j][k]]) == 1:
                return True
            return False
        
        n = len(words)
        maxLen, maxIndex = 1, 0
        currentMax = [1] + [0] * (n-1)
        previous = [-1] * n
        
        for j in range(n):
            auxVal, prevIndex = 1, -1
            for i in range(j):
                if follows(i, j) and currentMax[i] + 1 > auxVal:
                    auxVal = currentMax[i] + 1
                    prevIndex = i
                
            currentMax[j] = auxVal
            previous[j] = prevIndex
            
            if currentMax[j] > maxLen:
                maxLen = currentMax[j]
                maxIndex = j

        subSeq = []

        while maxIndex > -1:
            subSeq.append(words[maxIndex])
            maxIndex = previous[maxIndex]

        return subSeq[::-1]