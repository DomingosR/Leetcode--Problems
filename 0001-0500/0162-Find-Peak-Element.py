class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)

        def sign(i):
            if i < 0:
                return -1
            if i > 0:
                return 1
            return 0

        def variation(i):
            # nonlocal n
            if i == 0:
                return (-1, sign(nums[i+1] - nums[i]))
            if i == n-1:
                return (sign(nums[i-1] - nums[i]), -1)
            return (sign(nums[i-1] - nums[i]), sign(nums[i+1] - nums[i]))

        lowVal, highVal = 0, n-1
        while lowVal < highVal:
            midVal = lowVal + (highVal - lowVal) // 2
            currentVar = variation(midVal)
            if currentVar == (-1, -1):
                return midVal
            if currentVar[0] == 1:
                highVal = midVal
            else:
                lowVal = midVal + 1

        return lowVal