class Solution(object):
    def maxValueOfCoins(self, piles, k):
        n = len(piles)
        maxVal = defaultdict()

        # Function to return maximum value of 
        # numCoins coins from piles i, i + 1, ..., n - 1
        def dp(i, numCoins):
            if numCoins == 0 or i == n:
                return 0

            if (i, numCoins) in maxVal:
                return maxVal[(i, numCoins)]
            
            returnVal = dp(i+1, numCoins)
            currentVal = 0

            for j in range(min(len(piles[i]), numCoins)):
                currentVal += piles[i][j]
                returnVal = max(returnVal, currentVal + dp(i + 1, numCoins - j - 1))
            
            maxVal[(i, numCoins)] = returnVal
            return returnVal
        
        return dp(0, k)
            