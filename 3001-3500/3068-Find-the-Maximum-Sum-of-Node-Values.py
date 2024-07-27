class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        changeCount, totalSum, numChanges = 0, 0, 0
        minPosChange, maxNegChange = 2 ** 30, - 2 ** 30
        
        for num in nums:
            auxNum = (num ^ k)
            totalSum += max(num, auxNum)
            if auxNum >= num:
                numChanges += 1
                minPosChange = min(minPosChange, auxNum - num)
            else:
                maxNegChange = max(maxNegChange, auxNum - num)
        
        return totalSum + (numChanges % 2) * (-minPosChange + max(0, minPosChange + maxNegChange))