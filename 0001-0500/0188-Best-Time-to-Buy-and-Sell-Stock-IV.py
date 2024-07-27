import numpy as np

def maxTotalProfit(k, inputArray):
    numPrices = len(inputArray)
    if numPrices == 0:
        return 0

    maxValue = np.zeros((k+1)*numPrices).reshape(k+1, numPrices)

    for i in range(1, k+1):
        currentMax = -10000
        for d in range(1, numPrices):
            currentMax = max(currentMax, maxValue[i-1][d-1] - inputArray[d-1])
            maxValue[i][d] = max(currentMax + inputArray[d], maxValue[i][d-1])

    return int(maxValue[k][numPrices - 1])

class Solution(object):
    def maxProfit(self, k, prices):
        return maxTotalProfit(k, prices)