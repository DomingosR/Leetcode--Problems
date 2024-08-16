class Solution(object):
    def maximumUniqueSubarray(self, nums):
        n = len(nums)
        lastOccurrence = defaultdict(int)
        prevIndex = -1
        maxSum = 0
        cumSum = [0] * (n+1)
        
        for i, num in enumerate(nums):
            cumSum[i+1] = cumSum[i] + num
            if num in lastOccurrence:
                prevIndex = max(prevIndex, lastOccurrence[num])
            lastOccurrence[num] = i
            maxSum = max(cumSum[i+1] - cumSum[prevIndex+1], maxSum)
        
        return maxSum