class Solution(object):
    def maxScore(self, s):
        totalOnes = 1 if s[0] == "1" else 0
        runningDiff = (-1) if s[0] == "1" else 1
        maxDiff = runningDiff
        
        for i in range(1, len(s)):
            totalOnes += 1 if s[i] == "1" else 0
            if i < len(s) - 1:
                runningDiff += (-1) if s[i] == "1" else 1
                maxDiff = max(maxDiff, runningDiff)
                
        return maxDiff + totalOnes