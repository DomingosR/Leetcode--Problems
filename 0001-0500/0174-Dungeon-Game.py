class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        highVal = m * n * 1001
        
        minArrivingHealth = [[highVal] * (n+1) for _ in range(m+1)]
        minArrivingHealth[m][n-1] = 1
        minArrivingHealth[m-1][n] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                val1 = max(1, 1 - dungeon[i][j])
                val2 = minArrivingHealth[i+1][j] 
                val3 = minArrivingHealth[i][j+1]
                minArrivingHealth[i][j] = max(val1, min(val2, val3) - dungeon[i][j])
        
        return minArrivingHealth[0][0] 