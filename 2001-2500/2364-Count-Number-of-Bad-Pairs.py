class Solution(object):
    def countBadPairs(self, nums):
        n = len(nums)
        interceptCounter = Counter([nums[i] - i for i in range(len(nums))])
        return sum([val * (n - val) for val in interceptCounter.values()]) // 2