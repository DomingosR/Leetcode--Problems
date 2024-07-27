class Solution(object):
    def subsets(self, nums):
        numSubsets = [[]]
        
        for num in nums:
            n = len(numSubsets)
            for i in range(n):
                numSubsets.append(numSubsets[i] + [num])
                
        return numSubsets