class Solution(object):
    def isGood(self, nums):
        n = len(nums) - 1
        nums.sort()
        return all([nums[i] == min(i + 1, n) for i in range(n + 1)])