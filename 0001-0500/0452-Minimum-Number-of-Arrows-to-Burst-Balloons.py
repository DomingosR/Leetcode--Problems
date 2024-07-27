class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(reverse = True)
        currentArrow = points[0][0]
        arrowCount = 1

        for leftEnd, rightEnd in points:
            if currentArrow > rightEnd:
                currentArrow = leftEnd
                arrowCount += 1

        return arrowCount
