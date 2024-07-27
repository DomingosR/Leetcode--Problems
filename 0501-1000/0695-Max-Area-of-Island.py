from collections import deque

def maxAreaOfIsland(grid):
    numRows = len(grid)
    numCols = len(grid[0])
    
    queue = deque()
    
    def processCell():
        i, j = queue.pop()
        grid[i][j] = 0
        if i+1 < numRows and grid[i+1][j] == 1:
            queue.appendleft([i+1, j])
            grid[i+1][j] = 0
        if i-1 >= 0 and grid[i-1][j] == 1:
            queue.appendleft([i-1, j])
            grid[i-1][j] = 0
        if j+1 < numCols and grid[i][j+1] == 1:
            queue.appendleft([i, j+1])
            grid[i][j+1] = 0
        if j-1 >= 0 and grid[i][j-1] == 1:
            queue.appendleft([i, j-1])
            grid[i][j-1] = 0

    maxArea = 0
    for i in range(numRows):
        for j in range(numCols):
            if grid[i][j] == 1:
                tempArea = 0
                queue.appendleft([i, j])
                while queue:
                    processCell()
                    tempArea += 1
                maxArea = max(maxArea, tempArea)

    return maxArea

class Solution(object):
    def maxAreaOfIsland(self, grid):
        return maxAreaOfIsland(grid)