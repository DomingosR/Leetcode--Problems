class Solution(object):
    def stoneGameII(self, piles):
        numStones = len(piles)
        remainingSum = [0] * numStones
        remainingSum[-1] = piles[-1]

        for i in range(numStones-2, -1, -1):
            remainingSum[i] = remainingSum[i+1] + piles[i]

        optimalValues = defaultdict()
        
        def dp(i, m):
            if (i, m) in optimalValues:
                return optimalValues[(i, m)]
            if i + 2*m >= numStones:
                return remainingSum[i]
            returnVal = remainingSum[i]
            returnVal -= min(dp(i+j, max(m, j)) for j in range(1, 2*m+1))
            optimalValues[(i, m)] = returnVal
            return returnVal

        return dp(0, 1)