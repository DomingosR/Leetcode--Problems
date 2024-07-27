class Solution(object):
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n

        def slope(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            if x1 == x2:
                return float('inf')
            return 1.0 * (y2 - y1) / (x2 - x1)
        
        maxNumPoints = 2

        for i in range(n-1):
            currentPoint = points[i]
            slopes = defaultdict(int)
            for j in range(i+1, n):
                currentSlope = slope(points[j], currentPoint)
                slopes[currentSlope] += 1
            print(slopes)
            maxNumPoints = max(maxNumPoints, max(slopes.values()) + 1)

        return maxNumPoints