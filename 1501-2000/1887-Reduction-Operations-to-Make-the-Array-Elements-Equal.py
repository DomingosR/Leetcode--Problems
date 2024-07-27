class Solution(object):
    def reductionOperations(self, nums):
        numCounter = Counter(nums)
        auxData = [(i, numCounter[i]) for i in numCounter]
        auxData.sort(key = lambda x: -x[0])
        
        totalNums = 0
        totalOps = 0
        
        for i in range(len(auxData) - 1):
            n, count = auxData[i]
            totalNums += count
            totalOps += totalNums
            
        return totalOps