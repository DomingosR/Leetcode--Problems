class Solution(object):
    def maxTurbulenceSize(self, arr):
        def sign(num):
            return 1 if num > 0 else (-1 if num < 0 else 0)
        
        maxLen, currentSign, currentLen = 1, 0, 1
        
        for i in range(1, len(arr)):
            nextSign = sign(arr[i] - arr[i-1])
            if nextSign == 0:
                currentLen = 1
            else:
                if currentSign != 0 and currentSign == nextSign:
                    currentLen = 2
                else:
                    currentLen += 1
            currentSign = nextSign
            maxLen = max(maxLen, currentLen)
        
        return maxLen