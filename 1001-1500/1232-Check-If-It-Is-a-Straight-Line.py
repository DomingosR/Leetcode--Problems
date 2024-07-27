class Solution(object):
    def checkStraightLine(self, coordinates):
        n = len(coordinates)

        if all([coordinates[i][0] == coordinates[0][0] for i in range(n)]):
            return True

        if len([i for i in range(n) if coordinates[i][0] == coordinates[0][0]]) > 1:
            return False

        def slope(i):
            deltaY = coordinates[i][1] - coordinates[0][1]
            deltaX = coordinates[i][0] - coordinates[0][0]
            return 1.0 * deltaY / deltaX

        slopes = [slope(i) for i in range(1, n)]
        slopeSet = set(slopes)

        return (len(slopeSet) == 1)
