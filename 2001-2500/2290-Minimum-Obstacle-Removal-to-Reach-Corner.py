class Solution(object):
    def minimumObstacles(self, grid):
        numRows = len(grid)
        numCols = len(grid[0])

        maxNum = numRows * numCols + 1
        dist = [[maxNum] * numCols for _ in range(numRows)]
        dist[0][0] = 0
        
        cellQueue = deque([(0, 0, 0)])
        reachedEnd = False

        def processStep(currentRemovals, nextRow, nextCol):
            if numRows > nextRow >= 0 <= nextCol < numCols and dist[nextRow][nextCol] == maxNum:
                if grid[nextRow][nextCol] == 1:
                    dist[nextRow][nextCol] = currentRemovals + 1
                    cellQueue.appendleft((currentRemovals + 1, nextRow, nextCol))
                else:
                    dist[nextRow][nextCol] = currentRemovals
                    cellQueue.append((currentRemovals, nextRow, nextCol))   
            if nextRow == numRows - 1 and nextCol == numCols - 1:
                reachedEnd = True

        while cellQueue:
            removals, currentRow, currentCol = cellQueue.pop()
            processStep(removals, currentRow + 1, currentCol)
            processStep(removals, currentRow - 1, currentCol)
            processStep(removals, currentRow, currentCol + 1)
            processStep(removals, currentRow, currentCol - 1)
            if reachedEnd: 
                return dist[-1][-1]
   
        return dist[-1][-1]