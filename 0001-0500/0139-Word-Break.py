class Solution(object):
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        isFeasible = [True]
        for i in range(1, len(s) + 1):
            isFeasible.append(any([isFeasible[j] and s[j:i] in words for j in range(i)]))
        return isFeasible[-1]