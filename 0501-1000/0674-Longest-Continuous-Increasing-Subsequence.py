class Solution(object):
    def findLengthOfLCIS(self, nums):
        n = len(nums)
        maxLen = 1
        currentLen = 1

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                currentLen += 1
                maxLen = max(maxLen, currentLen)
            else:
                currentLen = 1
        
        return maxLen