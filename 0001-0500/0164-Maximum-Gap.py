import numpy as np

def maxGap(inputNums):
    numCount = len(inputNums)

    # Handle trivial cases
    if numCount < 2:
        return 0

    # Compute average gap between numbers, which
    # will form the basis for sorting numbers into buckets
    maxNum = max(inputNums)
    minNum = min(inputNums)
    if maxNum == minNum:
        return 0
    
    avgGap = (maxNum - minNum)/(1.0 * (numCount - 1))
    
    bucketMax = (minNum - 1) * np.ones(numCount - 1)
    bucketMin = (maxNum + 1) * np.ones(numCount - 1)
    bucketCount = np.zeros(numCount - 1)

    for i in range(numCount):
        currentNum = inputNums[i]
        currentBucket = min(int((currentNum - minNum) / avgGap), numCount - 2)
        
        bucketCount[currentBucket] += 1
        bucketMax[currentBucket] = max(currentNum, bucketMax[currentBucket])
        bucketMin[currentBucket] = min(currentNum, bucketMin[currentBucket])

    currentLow = minNum
    maxGap = max(bucketMax[0] - bucketMin[0], bucketMax[numCount - 2] - bucketMin[numCount - 2])
    i = 0

    while i < numCount - 1:
        while (bucketCount[i] == 0) and (i < numCount - 2):
            i += 1

        currentHigh = bucketMin[i]
        maxGap = max(maxGap, currentHigh - currentLow)
        currentLow = bucketMax[i]
        i += 1

    return int(maxGap)
    
class Solution(object):
    def maximumGap(self, nums):
        return maxGap(nums)