class Solution(object):
    def maximizeGreatness(self, nums):
        return len(nums) - max(Counter(nums).values())