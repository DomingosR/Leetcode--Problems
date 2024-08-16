class Solution(object):
    def smallestValue(self, n):
        allPrimes = [2]
        for i in range(3, 317):
            for j in range(len(allPrimes)):
                if i % allPrimes[j] == 0:
                    break
            else:
                allPrimes.append(i)
        
        seenValues = set()
        minVal = n
        
        def nextNum(n):
            currentSum, i = 0, 0
            while n > 1 and i < len(allPrimes):
                while n % allPrimes[i] == 0:
                    currentSum += allPrimes[i]
                    n //= allPrimes[i]
                i += 1
            if n > 1:
                currentSum += n
            return currentSum
        
        while n not in seenValues:
            seenValues.add(n)
            n = nextNum(n)
            minVal = min(minVal, n)
            
        return minVal