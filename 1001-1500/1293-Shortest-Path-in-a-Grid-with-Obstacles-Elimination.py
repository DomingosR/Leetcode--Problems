class Solution(object):
    def shortestPath(self, grid, k):
        numRows = len(grid)
        numCols = len(grid[0])
        cellsToProcess = deque([(0, 0, k, 0)])
        cellsVisited = set()

        if k >= numRows + numCols - 2:
            return numRows + numCols - 2

        def processStep(nextI, nextJ, remainingEliminations, stepsTaken):
            if 0 <= nextI < numRows and 0 <= nextJ < numCols and remainingEliminations >= grid[nextI][nextJ]:
                step = (nextI, nextJ, remainingEliminations - grid[nextI][nextJ], stepsTaken + 1)
                if step[0:3] not in cellsVisited:
                    cellsVisited.add(step[0:3])
                    cellsToProcess.appendleft(step)

        while cellsToProcess:
            i, j, remainingEliminations, stepsTaken = cellsToProcess.pop()
            if (i,j) == (numRows - 1, numCols - 1) :
                return stepsTaken

            processStep(i+1, j, remainingEliminations, stepsTaken)
            processStep(i-1, j, remainingEliminations, stepsTaken)
            processStep(i, j+1, remainingEliminations, stepsTaken)
            processStep(i, j-1, remainingEliminations, stepsTaken)

        return -1
