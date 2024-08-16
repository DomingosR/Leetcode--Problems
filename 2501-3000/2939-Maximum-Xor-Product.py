class Solution(object):
    def maximumXorProduct(self, a, b, n):
        p = 10 ** 9 + 7
        
        for currentBit in range(n-1, -1, -1):
            mask = (1 << currentBit)
            bitA, bitB = a & mask, b & mask
            
            if bitA == bitB == 0:
                a |= mask
                b |= mask
                
            elif bitA * bitB == 0:
                a -= bitA
                b -= bitB
                
                if a < b:
                    a += mask
                else:
                    b += mask
                 
        return a * b % p