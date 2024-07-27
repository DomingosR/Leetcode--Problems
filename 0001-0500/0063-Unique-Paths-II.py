class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        numWays = [[0] * n for _ in range(m)]
        numWays[0][0] = 1

        for sum in range(1, m+n-1):
            minCol = max(0, sum-m+1)
            maxCol = min(n-1, sum)
            for j in range(minCol, maxCol+1):
                i = sum-j
                if obstacleGrid[i][j] == 0:
                    if i > 0:
                        numWays[i][j] += numWays[i-1][j]
                    if j > 0:
                        numWays[i][j] += numWays[i][j-1]

        return numWays[-1][-1]
