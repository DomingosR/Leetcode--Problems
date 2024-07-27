class Solution(object):
    def countLargestGroup(self, n):
        def sumDigits(n):
            totalSum = 0
            while n > 0:
                totalSum += (n % 10)
                n //= 10
            return totalSum
        
        sumCounter = Counter()
        
        for i in range(1, n+1):
            sumCounter[sumDigits(i)] += 1
        
        maxVal = max(sumCounter.values())
        return len([num for num in sumCounter.keys() if sumCounter[num] == maxVal])