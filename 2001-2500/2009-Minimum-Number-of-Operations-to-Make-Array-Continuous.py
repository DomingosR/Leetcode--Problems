class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        auxList = list(set(nums))
        auxList.sort()
        minOps = n - 1
        
        for i, minVal in enumerate(auxList):
            maxVal = minVal + n - 1
            index = bisect_right(auxList, maxVal)
            uniqueCount = index - i
            minOps = min(minOps, n - uniqueCount)
        
        return minOps