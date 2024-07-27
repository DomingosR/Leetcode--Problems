class Solution(object):
    def minimizeXor(self, num1, num2):
        def bitCount(num):
            count = 0
            while num > 0:
                count += num & 1
                num >>= 1
            return count
        
        def mostSignificantBit(num):
            # Returns i for num = (1 << i)
            bitNum = 0
            while num > 0:
                bitNum += 1
                num >>= 1
            return bitNum
        
        numBits1, numBits2 = bitCount(num1), bitCount(num2)
        bitsToRemove, bitsToAdd = min(numBits1, numBits2), max(numBits2 - numBits1, 0)
        x = 0
        
        currentBit = mostSignificantBit(num1)
        while bitsToRemove:
            if num1 & (1 << currentBit):
                x ^= (1 << currentBit)
                bitsToRemove -= 1
            currentBit -= 1
        
        currentBit = 0
        while bitsToAdd:
            if not num1 & (1 << currentBit):
                x |= (1 << currentBit)
                bitsToAdd -= 1
            currentBit += 1
        
        return x