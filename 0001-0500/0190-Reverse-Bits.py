def reverseAllBits(n):
    returnVal = 0
    for i in xrange(32):
        returnVal = (returnVal << 1) + (n & 1)
        n >>=1
    
    return returnVal

class Solution:
    def reverseBits(self, n):
        return reverseAllBits(n)