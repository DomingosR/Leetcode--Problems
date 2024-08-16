class Solution(object):
    def balancedStringSplit(self, s):
        countSubstr = 0
        currentCount = 0
        
        for char in s:
            currentCount += (1 if char == "R" else -1)
            countSubstr += (currentCount == 0)
            
        return countSubstr