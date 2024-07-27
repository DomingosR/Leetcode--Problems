class Solution(object):
    def countBits(self, n):
        numOneBits = [0] * (n+1)
        
        for i in range(1, n+1):
            numOneBits[i] = (numOneBits[i-1] + 1) if (i % 2) else numOneBits[i//2]
            
        return numOneBits