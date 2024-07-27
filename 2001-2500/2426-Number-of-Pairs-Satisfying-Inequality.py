class Solution(object):
    def numberOfPairs(self, nums1, nums2, diff):
        n = len(nums1)
        numsDiff = [nums1[i] - nums2[i] for i in range(n)]
        numsValues = []
        pairsCount = 0
        
        for i in range(n):
            pairsToAdd = bisect.bisect(numsValues, numsDiff[i] + diff)
            pairsCount += pairsToAdd
            insertPoint = bisect.bisect(numsValues, numsDiff[i])
            numsValues.insert(insertPoint, numsDiff[i])
        
        return pairsCount