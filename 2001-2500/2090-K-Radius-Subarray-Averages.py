class Solution(object):
    def getAverages(self, nums, k):
        n = len(nums)
        avgArray = [-1 for _ in range(n)]
        
        if n >= 2*k+1:
            currentSum = sum(nums[:2*k+1])
            for i in range(k, n-k):
                avgArray[i] = currentSum // (2*k+1)
                if i < n-k-1:
                    currentSum += (nums[i+k+1] - nums[i-k])
        
        return avgArray