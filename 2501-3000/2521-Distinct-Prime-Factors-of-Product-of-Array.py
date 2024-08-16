class Solution(object):
    def distinctPrimeFactors(self, nums):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        
        primeSet = set()
        for num in nums:
            for p in primes:
                if num % p == 0:
                    primeSet.add(p)
                    while num % p == 0:
                        num //= p
            
                    if num == 1:
                        break
                
            if num > 1:
                primeSet.add(num)
                
        return len(primeSet)