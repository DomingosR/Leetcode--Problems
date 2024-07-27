class Solution(object):
    def longestStrChain(self, words):
        words.sort(key = lambda x: (len(x), x))
        maxLen = {}
        overallMax = 1
        
        for word in words:
            maxLen[word] = max(maxLen.get(word[:i] + word[i+1:], 0) + 1 for i in range(len(word)))
            overallMax = max(overallMax, maxLen[word])
        
        return overallMax
