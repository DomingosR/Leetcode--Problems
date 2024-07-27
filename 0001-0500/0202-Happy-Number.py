class Solution(object):
    def isHappy(self, n):
        if n == 1:
            return True
        
        prevValues = set([n])

        while True:
            sumSquares = 0
            while n > 0:
                sumSquares += (n % 10) ** 2
                n //= 10
            if sumSquares == 1:
                return True
            if sumSquares in prevValues:
                return False
            prevValues.add(sumSquares)
            n = sumSquares