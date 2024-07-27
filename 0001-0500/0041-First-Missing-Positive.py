class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1
        
        for i in range(n):
            if 1 <= abs(nums[i]) <= n:
                index = abs(nums[i]) - 1
                nums[index] *= (-1 if nums[index] > 0 else 1)
        
        for i in range(n):
            if nums[i] > 0:
                return i+1
        
        return n+1