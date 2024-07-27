class Solution(object):
    def minPatches(self, nums, n):
        nextMissing, addedCount, i = 1, 0, 0
        
        while nextMissing <= n:
            if i < len(nums) and nums[i] <= nextMissing:
                nextMissing += nums[i]
                i += 1
            else:
                nextMissing += nextMissing
                addedCount += 1
        
        return addedCount