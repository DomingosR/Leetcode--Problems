class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
            
        primes = [2, 3, 5]

        for p in primes:
            while n % p == 0:
                n = n //p
        
        return n == 1