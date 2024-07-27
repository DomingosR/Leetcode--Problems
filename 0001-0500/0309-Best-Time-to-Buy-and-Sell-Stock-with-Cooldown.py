class Solution(object):
    def maxProfit(self, prices):
        # Solution notes:
        #
        # There are three possible states for the investor at the end of a day:
        # > 0: Holding the stock
        # > 1: Not holding the stock, just having sold it (thus restricted from buying the next day)
        # > 2: Not holding the stock, but unrestricted from buying the next day
        #
        # mCCF stands for maximumCumulativeCashFlow of a strategy that at the end of day i is in state s
        # (where s is 0, 1 or 2).
        
        n = len(prices)
        if n <= 1:
            return 0

        mCCF = [[0, 0, 0] for _ in range(n)]
        mCCF[0][0] = - prices[0]

        for i in range(1, n):
            mCCF[i][0] = max(mCCF[i-1][0],                 # Held the stock the previous day, continued to hold it
                             mCCF[i-1][2] - prices[i])     # Just bought the stock
            mCCF[i][1] = mCCF[i-1][0] + prices[i]          # Held the stock the previous day, just sold it
            mCCF[i][2] = max(mCCF[i-1][1],                 # Was restricted the previous day, became unrestricted
                             mCCF[i-1][2])                 # Was unrestricted the previous day, didn't act
        
        return max(mCCF[-1])