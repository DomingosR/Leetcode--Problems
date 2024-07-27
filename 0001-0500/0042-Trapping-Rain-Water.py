class Solution(object):
    def trap(self, inputHeights):
        maxHeight = max(inputHeights)
        numWalls = len(inputHeights)
        totalWaterTrapped = 0

        i = 0
        maxHeightLeft = 0
        while inputHeights[i] < maxHeight:
            maxHeightLeft = max(maxHeightLeft, inputHeights[i])
            totalWaterTrapped += (maxHeightLeft - inputHeights[i])
            i += 1

        j = numWalls - 1
        maxHeightRight = 0
        while inputHeights[j] < maxHeight:
            maxHeightRight = max(maxHeightRight, inputHeights[j])
            totalWaterTrapped += (maxHeightRight - inputHeights[j])
            j -= 1

        if i < j:
            totalWaterTrapped += maxHeight * (j - i) - sum(inputHeights[i:j])

        return totalWaterTrapped