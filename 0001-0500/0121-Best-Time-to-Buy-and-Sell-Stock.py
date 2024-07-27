class Solution(object):
    def maxProfit(self, prices):
        currentMin = prices[0]
        maxProfit = 0
        
        for p in prices:
            maxProfit = max(maxProfit, p - currentMin)
            currentMin = min(currentMin, p)
            
        return maxProfit