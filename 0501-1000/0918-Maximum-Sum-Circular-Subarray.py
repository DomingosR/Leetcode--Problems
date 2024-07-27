class Solution(object):
    def maxSubarraySumCircular(self, nums):
        overallTotal = 0
        currentMax = 0
        overallMax = nums[0]
        currentMin = 0
        overallMin = nums[0]

        for num in nums:
            overallTotal += num
            currentMax = max(currentMax + num, num)
            currentMin = min(currentMin + num, num)
            overallMax = max(overallMax, currentMax)
            overallMin = min(overallMin, currentMin)

        if overallMax > 0:
            return max(overallMax, overallTotal - overallMin)
        else:
            return overallMax
