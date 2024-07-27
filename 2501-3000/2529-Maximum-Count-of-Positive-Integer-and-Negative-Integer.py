class Solution(object):
    def maximumCount(self, nums):
        n = len(nums)
        negCount = bisect_left(nums, 0)
        posCount = n - bisect_right(nums, 0)
        return max(negCount, posCount)
