class Solution(object):
    def longestSubarray(self, nums):
        n = len(nums)
        zeroPos = [i for i in range(n) if nums[i] == 0]
        if len(zeroPos) <= 1:
            return n-1
        
        zeroPos = [-1] + zeroPos + [n]
        auxCount = len(zeroPos)
        auxLen = [zeroPos[i+2] - zeroPos[i] for i in range(auxCount-2)]
        return max(auxLen) - 2