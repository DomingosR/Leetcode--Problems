class Solution(object):
    def countTriples(self, n):
        def isSquare(num):
            auxNum = int(sqrt(num))
            return auxNum * auxNum == num
            
        tripleCount = 0
        
        for c in range(1, n+1):
            totalSum = c ** 2
            for a in range(1, c):
                if isSquare(totalSum - a ** 2):
                    tripleCount += 1
                        
        return tripleCount