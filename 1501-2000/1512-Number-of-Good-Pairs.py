class Solution(object):
    def numIdenticalPairs(self, nums):
        return sum([val*(val-1)//2 for val in Counter(nums).values()])