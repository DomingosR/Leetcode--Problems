class Solution(object):
    def singleNumber(self, nums):
        numCounter = Counter(nums)
        return [i for i in numCounter.keys() if numCounter[i] == 1][0]