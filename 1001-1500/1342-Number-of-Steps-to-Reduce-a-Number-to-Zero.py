class Solution(object):
    def numberOfSteps(self, num):
        numSteps = 0
        while num > 0:
            numSteps += 1
            num = (num // 2) if (num % 2 == 0) else (num - 1)
        
        return numSteps