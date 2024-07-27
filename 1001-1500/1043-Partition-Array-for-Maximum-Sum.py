class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        n = len(arr)
        overallMax = [0] * (n+1)
        
        for i in range(1, n+1):
            currentMax = 0
            for j in range(1, min(k, i)+1):
                currentMax = max(currentMax, arr[i - j])
                overallMax[i] = max(overallMax[i], overallMax[i-j] + currentMax * j)
        
        return overallMax[-1]