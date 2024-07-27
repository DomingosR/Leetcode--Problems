class Solution(object):
    def findIntegers(self, n):
        preComputed = {0: 1, 1: 2, 2: 3}
        for k in range(2, 32):
            preComputed[2**k-1] = preComputed[2**(k-1)-1] + preComputed[2**(k-2)-1]
        
        def powerOf2(n):
            k = -1
            while n >= 1:
                n >>= 1
                k += 1
            return k
        
        def processNum(n):
            if n in preComputed:
                return preComputed[n]
            
            k = powerOf2(n)
            r = min(n - 2**k, 2**(k-1) - 1)
            finalVal = processNum(2**k-1) + processNum(r)
            preComputed[n] = finalVal
            return finalVal
        
        return processNum(n)