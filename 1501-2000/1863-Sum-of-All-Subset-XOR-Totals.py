class Solution(object):
    def subsetXORSum(self, nums):
        n, overallOR = len(nums), 0
        for num in nums:
            overallOR |= num
            
        return overallOR * (1 << n-1)