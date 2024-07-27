class Solution(object):
    def isPossibleToCutPath(self, grid):
        m, n = len(grid), len(grid[0])
        pathsFromOrigin = [[0] * n for _ in range(m)]
        pathsFromOrigin[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    pathsFromOrigin[i][j] += (0 if i == 0 else pathsFromOrigin[i-1][j]) + \
                                             (0 if j == 0 else pathsFromOrigin[i][j-1])
        
        totalPaths = pathsFromOrigin[-1][-1]
        if totalPaths == 0:
            return True
        
        pathsFromDest = [[0] * n for _ in range(m)]
        pathsFromDest[m-1][n-1] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    pathsFromDest[i][j] += (0 if i == m-1 else pathsFromDest[i+1][j]) + \
                                           (0 if j == n-1 else pathsFromDest[i][j+1])   
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i > 0 or j > 0) and (i < m-1 or j < n-1):
                    if pathsFromDest[i][j] * pathsFromOrigin[i][j] == totalPaths:
                        return True
                    
        return False