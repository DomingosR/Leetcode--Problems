class Solution(object):
    def numSteps(self, s):
        numSteps = 0
        n = int(s, 2)
        
        while n > 1:
            numSteps += 1
            n = (n // 2 if n % 2 == 0 else n + 1)
            
        return numSteps