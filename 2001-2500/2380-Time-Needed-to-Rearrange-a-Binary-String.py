class Solution(object):
    def secondsToRemoveOccurrences(self, s):
        n = len(s)
        zeroPos = [i for i in range(n) if s[i] == "0"] + [n]
        numZeros = len(zeroPos)
        seconds = 0
        
        while zeroPos[0] < n - numZeros + 1:
            for i in range(numZeros - 1):
                zeroPos[i] = min(zeroPos[i] + 1, zeroPos[i+1] - 1)
            seconds += 1
            
        return seconds