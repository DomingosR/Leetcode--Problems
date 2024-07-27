class Solution(object):
    def arraySign(self, nums):
        if 0 in nums:
            return 0
        countNeg = len([1 for i in nums if i < 0])
        return 1 if countNeg % 2 == 0 else -1
