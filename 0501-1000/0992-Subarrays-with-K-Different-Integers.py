class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def subArraysWithAtMostK(numsArg, k):
            valueCounter = Counter()
            numSubArrays = 0
            j = 0
            
            for i in range(len(numsArg)):
                if valueCounter[numsArg[i]] == 0:
                    k -= 1
                valueCounter[numsArg[i]] += 1
                while k < 0:
                    valueCounter[numsArg[j]] -= 1
                    if valueCounter[numsArg[j]] == 0:
                        k += 1
                    j += 1
                numSubArrays += (i - j + 1)
        
            return numSubArrays
        
        return subArraysWithAtMostK(nums, k) - subArraysWithAtMostK(nums, k-1)