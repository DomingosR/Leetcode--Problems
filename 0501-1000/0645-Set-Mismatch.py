class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        totalSum = sum(nums)
        sumSet = sum(set(nums))
        return [totalSum - sumSet, n * (n+1) // 2 - sumSet]