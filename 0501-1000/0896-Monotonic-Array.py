class Solution(object):
    def isMonotonic(self, nums):
        if len(nums) == 1:
            return True

        maxVal = -2*10**5 - 1
        minVal =  2*10**5 + 1

        for i in range(len(nums) - 1):
            currDiff = nums[i+1] - nums[i]
            maxVal = max(maxVal, currDiff)
            minVal = min(minVal, currDiff)
            if minVal < 0 < maxVal:
                return False

        return True
