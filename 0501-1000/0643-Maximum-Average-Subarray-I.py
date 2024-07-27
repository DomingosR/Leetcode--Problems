class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        maxSum = sum(nums[:k])
        currentSum = maxSum
        
        for i in range(k, n):
            currentSum += (nums[i] - nums[i-k])
            maxSum = max(maxSum, currentSum)
        
        return 1.0 * maxSum / k