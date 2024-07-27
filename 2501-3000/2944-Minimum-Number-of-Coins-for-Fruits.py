class Solution(object):
    def minimumCoins(self, prices):
        previousValues = defaultdict(int)
        n = len(prices)
        
        # The following function returns the minimum value of collecting
        # fruits i through n-1 while purchasing the i-th fruit.
        def minCost(i):
            if i not in previousValues:
                if i >= n:
                    previousValues[i] = 0
                else:
                    # If we pay for fruit i, we get i + 1, i + 2, ..., 2 * i + 1.
                    # Then, we will have to pay for one of
                    # i + 1, i + 2, ..., 2 * i + 2 in order to collect 2 * i + 2
                    currentCost = prices[i] + min([minCost(j) for j in range(i + 1, 2 * i + 3)])
                    previousValues[i] = currentCost
            
            return previousValues[i]

        return minCost(0)