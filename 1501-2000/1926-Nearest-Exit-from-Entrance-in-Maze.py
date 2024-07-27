class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        numRows = len(maze)
        numCols = len(maze[0])

        entranceCell = tuple(entrance)
        visitedCells = {entranceCell}

        cellQueue = deque()
        cellQueue.appendleft((entranceCell, 0))
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        exitRows = {0, numRows - 1}
        exitCols = {0, numCols - 1}

        def isCellValid(indCell):
            if not numRows > indCell[0] >= 0 <= indCell[1] < numCols:
                return False
            if indCell in visitedCells:
                return False
            if maze[indCell[0]][indCell[1]] == "+":
                return False
            return True

        def isExit(indCell):
            return (indCell[0] in exitRows) or (indCell[1] in exitCols)

        while cellQueue:
            currentCell, currentSteps = cellQueue.pop()
            for direction in directions:
                nextCell = (currentCell[0] + direction[0], currentCell[1] + direction[1])
                if isCellValid(nextCell):
                    if isExit(nextCell):
                        return currentSteps + 1
                    else:
                        cellQueue.appendleft((nextCell, currentSteps + 1))
                        visitedCells.add(nextCell)

        return -1