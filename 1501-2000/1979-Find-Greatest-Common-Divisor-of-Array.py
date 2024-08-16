class Solution(object):
    def findGCD(self, nums):
        minVal, maxVal = nums[0], nums[0]
        
        for num in nums:
            minVal, maxVal = min(minVal, num), max(maxVal, num)
            
        while minVal:
            maxVal, minVal = minVal, maxVal % minVal
            
        return maxVal