class Solution(object):
    def maximumCandies(self, candies, k):
        totalCandies = sum(candies)
        if totalCandies < k:
            return 0
        
        pileCounter = Counter(candies)
        
        def maxNumChildren(numCandies):
            return sum([pileCounter[val] * (val // numCandies) for val in pileCounter])
        
        lowVal, highVal =  1, sum(candies) // k
        iterNo = 0
        while lowVal < highVal:
            midVal = highVal - (highVal - lowVal) // 2
            if maxNumChildren(midVal) >= k:
                lowVal = midVal
            else:
                highVal = midVal - 1
            iterNo += 1
                
        return lowVal