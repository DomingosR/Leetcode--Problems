class Solution(object):
    def countPrimes(self, n):
        if n < 3:
            return 0
        
        primes = [True] * n
        primes[0] = False
        primes[1] = False
        
        for p in range(2, int(n**0.5) + 1):
            if primes[p]:
                primes[p * p: n: p] = [False] * len(primes[p * p: n: p])
        
        return sum(primes)