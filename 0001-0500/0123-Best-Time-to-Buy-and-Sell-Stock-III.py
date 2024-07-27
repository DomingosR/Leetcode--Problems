import numpy as np

def maxTotalProfitV2(inputArray):
    numPrices = len(inputArray)

    minPriceL = inputArray[0]
    maxProfitL = 0

    minPriceR = -inputArray[numPrices - 1]
    maxProfitR = 0

    maxProfitArray = np.zeros(numPrices+1)

    for i in range(1, numPrices):
        maxProfitL = max(inputArray[i] - minPriceL, maxProfitL)
        maxProfitArray[i+1] = maxProfitArray[i+1] + maxProfitL
        minPriceL = min(inputArray[i], minPriceL)

        j = numPrices - (i + 1)

        maxProfitR = max(-inputArray[j] - minPriceR, maxProfitR)
        maxProfitArray[j] = maxProfitArray[j] + maxProfitR
        minPriceR = min(-inputArray[j], minPriceR)

    return int(max(maxProfitArray))

class Solution(object):
    def maxProfit(self, prices):
        return maxTotalProfitV2(prices)