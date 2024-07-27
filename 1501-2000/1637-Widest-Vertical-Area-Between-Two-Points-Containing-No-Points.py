class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        xVals = sorted([point[0] for point in points])
        return max([xVals[i] - xVals[i-1] for i in range(1, len(xVals))])