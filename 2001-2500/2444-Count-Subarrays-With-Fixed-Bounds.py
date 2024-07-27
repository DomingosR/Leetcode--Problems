class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        numSubArrays = 0
        # Note: OOB stands for out-of-bounds
        lastMinIndex, lastMaxIndex, lastOOBIndex = -1, -1, -1
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                lastOOBIndex = i
            if num == minK:
                lastMinIndex = i
            if num == maxK:
                lastMaxIndex = i
            auxVal = min(lastMinIndex, lastMaxIndex) - lastOOBIndex
            numSubArrays += max(0, auxVal)
            
        return numSubArrays