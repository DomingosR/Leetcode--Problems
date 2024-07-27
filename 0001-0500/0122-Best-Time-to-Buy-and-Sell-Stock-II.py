class Solution(object):
    def maxProfit(self, prices):
        # There are two possible portfolio positions at the end of day i, 0 or 1,
        # representing the number of shares the investor holds.
        #
        # MCCF[s] represents the maximum cumulative cash flow of a sequence of
        # trades that end in state s.

        n = len(prices)
        if n == 1:
            return 0

        currentMCCF = [0, -prices[0]]

        for i in range(1, n):
            nextMCCF = [0, 0]
            nextMCCF[0] = max(currentMCCF[0],                    # Didn't own stock in previous period, didn't buy it this period
                              currentMCCF[1] + prices[i])        # Owned the stock at the end of previous period, sold it this period
            nextMCCF[1] = max(currentMCCF[1],                    # Owned stock in previous period, continued to hold it this period
                              currentMCCF[0] - prices[i])        # Didn't own the stock at the end of previous period, bought it this period
            currentMCCF = nextMCCF
        
        return max(currentMCCF)