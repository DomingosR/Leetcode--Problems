class Solution(object):
    def minSwaps(self, nums):
        n, windowLen = len(nums), sum(nums)
        minZeroCount = windowLen - sum(nums[:windowLen])
        currentZeroCount = minZeroCount
        
        for i in range(n - 1):
            currentZeroCount += (nums[i] - nums[(i + windowLen) % n])
            minZeroCount = min(minZeroCount, currentZeroCount)
            
        return minZeroCount