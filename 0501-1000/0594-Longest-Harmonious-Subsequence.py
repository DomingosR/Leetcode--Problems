class Solution(object):
    def findLHS(self, nums):
        maxLength = 0
        numCounter = Counter(nums)
        
        return max([numCounter[val] + numCounter[val+1] for val in numCounter if val+1 in numCounter] + [0])