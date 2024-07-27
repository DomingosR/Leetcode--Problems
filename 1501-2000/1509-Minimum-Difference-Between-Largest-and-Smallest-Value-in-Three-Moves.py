class Solution(object):
    def minDifference(self, nums):
        if len(nums) < 5:
            return 0
        
        nums.sort()
        
        return min([nums[-4 + i] - nums[i] for i in range(4)])