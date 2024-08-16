class Solution(object):
    def isThree(self, n):
        if n == 1:
            return False
        
        sqrtVal = int(sqrt(n))
        
        if sqrtVal * sqrtVal != n:
            return False
        
        for i in range(2, int(sqrt(sqrtVal) + 1)):
            if sqrtVal % i == 0:
                return False
            
        return True