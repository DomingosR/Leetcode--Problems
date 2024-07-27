class Solution(object):
    def findMaxK(self, nums):
        return max([n for n in nums if n > 0 and (-n) in nums] + [-1])
