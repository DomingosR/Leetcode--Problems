class Solution(object):
    def hammingWeight(self, n):
        returnVal = 0
        while n:
            n = n & (n-1)
            returnVal += 1
        return returnVal