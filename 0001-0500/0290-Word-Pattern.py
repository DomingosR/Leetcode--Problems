class Solution(object):
    def wordPattern(self, pattern, s):
        splitS = s.split(" ")
        if len(splitS) != len(pattern):
            return False
            
        letterDict = defaultdict()
        wordDict = defaultdict()
        n = len(pattern)

        for i in range(n):
            if pattern[i] in letterDict.keys() and letterDict[pattern[i]] != splitS[i]:
                return False
            if splitS[i] in wordDict.keys() and wordDict[splitS[i]] != pattern[i]:
                return False

            letterDict[pattern[i]] = splitS[i]
            wordDict[splitS[i]] = pattern[i]
        
        return True