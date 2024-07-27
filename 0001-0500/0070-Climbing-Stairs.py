class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n

        prevNum = 1
        lastNum = 2
        for i in range(2, n):
            prevNum, lastNum = lastNum, prevNum + lastNum
        
        return lastNum