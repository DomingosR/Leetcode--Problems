class Solution(object):
    def numSplits(self, s):
        n = len(s)
        leftCounter, rightCounter = Counter(s), Counter()
        numDistinctLeft, numDistinctRight = len(leftCounter), 0
        numSplits = 0
        
        for i in range(n-1, -1, -1):
            char = s[i]
            if char not in rightCounter:
                numDistinctRight += 1
            if leftCounter[char] == 1:
                numDistinctLeft -= 1
            rightCounter[char] += 1
            leftCounter[char] -= 1
            
            if numDistinctRight == numDistinctLeft:
                numSplits += 1
            
            if numDistinctLeft < numDistinctRight:
                break
                
        return numSplits