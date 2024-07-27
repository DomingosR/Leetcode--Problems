class Solution(object):
    def findMiddleIndex(self, nums):
        n, totalSum = len(nums), sum(nums)
        currentSum, i = 0, 0
        
        while i < n:
            if currentSum + nums[i] == totalSum - currentSum:
                return i
            currentSum += nums[i]
            i += 1
            
        return -1