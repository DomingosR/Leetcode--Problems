class Solution(object):
    def isBoomerang(self, points):
        x0, y0 = points[0]
        x1, y1 = points[1]
        x2, y2 = points[2]

        return (x2 - x0) * (y1 - y0) != (y2 - y0) * (x1 - x0)
