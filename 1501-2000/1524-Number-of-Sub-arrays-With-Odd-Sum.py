class Solution(object):
    def numOfSubarrays(self, arr):
        n = len(arr)
        currentSumCount = [0, 0]
        totalOddSum = 0
        
        for i, num in enumerate(arr):
            nextSumCount = [0, 0]
            if num % 2:
                nextSumCount[0] = currentSumCount[1]
                nextSumCount[1] = currentSumCount[0] + 1
            else:
                nextSumCount[0] = currentSumCount[0] + 1
                nextSumCount[1] = currentSumCount[1]  
                
            totalOddSum += nextSumCount[1]
            currentSumCount = nextSumCount
        
        return totalOddSum % (10 ** 9 + 7)