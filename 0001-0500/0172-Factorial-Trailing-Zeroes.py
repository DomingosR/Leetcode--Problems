class Solution(object):
    def trailingZeroes(self, n):
        numZeroes = 0
        
        while n > 4:
            numZeroes += (n // 5)
            n //= 5
        
        return numZeroes