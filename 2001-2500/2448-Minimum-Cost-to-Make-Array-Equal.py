class Solution(object):
    def minCost(self, nums, cost):
        allInfo = zip(nums, cost)
        
        def cost(val):
            return sum(abs(num - val) * indCost for num, indCost in allInfo)
        
        lowVal, highVal = min(nums), max(nums)
        currentMin = cost(lowVal)
        
        while lowVal < highVal:
            midVal = (lowVal + highVal) // 2
            testVal1 = cost(midVal)
            testVal2 = cost(midVal + 1)
            currentMin = min(testVal1, testVal2)
            
            if testVal1 < testVal2:
                highVal = midVal
            else:
                lowVal = midVal + 1
        
        return currentMin