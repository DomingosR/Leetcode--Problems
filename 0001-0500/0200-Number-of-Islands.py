class Solution(object):
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        numIslands = 0
        cellQueue = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    numIslands += 1
                    grid[i][j] = "0"
                    
                    cellQueue.appendleft((i, j))
                    while cellQueue:
                        currI, currJ = cellQueue.pop()
                        if currI > 0 and grid[currI - 1][currJ] == "1":
                            grid[currI - 1][currJ] = "0"
                            cellQueue.appendleft((currI - 1, currJ))
                        if currI < m - 1 and grid[currI + 1][currJ] == "1":
                            grid[currI + 1][currJ] = "0"
                            cellQueue.appendleft((currI + 1, currJ))  
                        if currJ > 0 and grid[currI][currJ - 1] == "1":
                            grid[currI][currJ - 1] = "0"
                            cellQueue.appendleft((currI, currJ - 1))  
                        if currJ < n - 1 and grid[currI][currJ + 1] == "1":
                            grid[currI][currJ + 1] = "0"
                            cellQueue.appendleft((currI, currJ + 1))                               
                  
        return numIslands