class Solution(object):
    def maxArea(self, height):
        n = len(height)
        leftEnd = 0
        rightEnd = n-1
        maxWater = (rightEnd - leftEnd) * min(height[leftEnd], height[rightEnd])

        while leftEnd < rightEnd:
            if height[leftEnd] < height[rightEnd]:
                leftEnd += 1
            else:
                rightEnd -= 1
            maxWater = max(maxWater, (rightEnd - leftEnd) * min(height[leftEnd], height[rightEnd]))

        return maxWater
