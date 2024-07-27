class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cumSum = list(accumulate(nums))
        if cumSum[-1] < target:
            return 0
        
        n = len(cumSum)
        cumSum = [0] + cumSum
        i, j = 1, 0
        
        while cumSum[i] < target:
            i += 1
        
        minLen = i
        
        while i < n+1:
            while j < i and cumSum[i] - cumSum[j+1] >= target:
                j += 1
            minLen = min(minLen, i - j)
            i += 1
              
        return minLen