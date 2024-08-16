class Solution(object):
    def isOneBitCharacter(self, bits):
        n = len(bits)
        onesCount = 0
        i = n - 2
        
        while i >= 0 and bits[i] == 1:
            onesCount += 1
            i -= 1
            
        return onesCount % 2 == 0