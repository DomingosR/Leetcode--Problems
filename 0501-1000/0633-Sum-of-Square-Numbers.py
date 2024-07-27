class Solution(object):
    def judgeSquareSum(self, c):
        def isSquare(n):
            n1 = int(sqrt(n))
            return n1 * n1 == n
        
        for i in range(int(sqrt(c)) + 1):
            if isSquare(c - i ** 2):
                return True
            
        return False