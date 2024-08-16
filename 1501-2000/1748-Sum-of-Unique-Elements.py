class Solution(object):
    def sumOfUnique(self, nums):
        numCounter = Counter(nums)
        return sum([val for val in numCounter if numCounter[val] == 1])