class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        minTime = 0
        for i in range(len(points) - 1):
            minTime += max(abs(points[i][0] - points[i+1][0]), \
                           abs(points[i][1] - points[i+1][1]))
        return minTime
