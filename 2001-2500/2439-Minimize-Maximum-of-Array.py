class Solution(object):
    def minimizeArrayValue(self, nums):
        n = len(nums)
        totalSum = 0
        overallMax = 0
        
        for i in range(n):
            totalSum += nums[i]
            overallMax = max(overallMax, (totalSum + i)//(i + 1))
        
        return overallMax