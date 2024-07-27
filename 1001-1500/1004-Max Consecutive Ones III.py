class Solution(object):
    def longestOnes(self, nums, k):
        zeroLocations = deque()
        zeroLocations.appendleft(-1)
        maxLen = 0
        
        for i, n in enumerate(nums):
            if n == 0:
                if len(zeroLocations) == k+1:
                    maxLen = max(maxLen, i - 1 - zeroLocations.pop())
                zeroLocations.appendleft(i)
                
        maxLen = max(maxLen, len(nums) - 1 - zeroLocations.pop())
        return maxLen