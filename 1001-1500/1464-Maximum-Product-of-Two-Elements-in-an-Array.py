class Solution(object):
    def maxProduct(self, nums):
        maxNum = -1
        minNum = -1
        
        for n in nums:
            if n >= maxNum:
                maxNum, minNum = n, maxNum
            elif n >= minNum:
                minNum = n
                
        return (maxNum - 1) * (minNum - 1)