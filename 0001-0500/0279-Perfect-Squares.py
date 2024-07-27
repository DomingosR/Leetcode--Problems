class Solution(object):
    def numSquares(self, n):
        def isSquare(num):
            aux = math.trunc(sqrt(num))
            return aux * aux == num
        
        if isSquare(n):
            return 1
        
        for i in range(math.trunc(sqrt(n)) + 1):
            if isSquare(n - i * i):
                return 2
            
        auxNum = n
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        
        return 3