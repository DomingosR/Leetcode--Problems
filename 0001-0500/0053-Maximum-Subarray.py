class Solution(object):
    def maxSubArray(self, nums):
        maxVal = - 10**4 - 1
        currMax = 0

        n = len(nums)
        for i in range(n):
            currMax = max(currMax + nums[i], nums[i])
            maxVal = max(maxVal, currMax)
        return maxVal
