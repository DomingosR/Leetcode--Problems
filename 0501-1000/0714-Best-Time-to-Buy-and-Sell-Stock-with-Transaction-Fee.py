class Solution(object):
    def maxProfit(self, prices, fee):
        n = len(prices)
        maxWith, maxWithout = - prices[0] - fee, 0
        
        for i in range(1, n):
            maxWith, maxWithout = max(maxWith, maxWithout - prices[i] - fee), \
                                  max(maxWithout, maxWith + prices[i])
        
        return maxWithout 