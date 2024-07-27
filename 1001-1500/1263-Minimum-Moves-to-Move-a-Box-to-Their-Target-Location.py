class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        box, person, target = (-1, -1), (-1, -1), (-1, -1)
        directions = [1, 0, -1, 0, 1]

        def findElements():
            nonlocal target, box, person
            found = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == "T": target = (i, j)
                    if grid[i][j] == "B": box = (i, j)
                    if grid[i][j] == "S": person = (i, j)

        def locationValid(i, j):
            return m > i >= 0 <= j < n and grid[i][j] != "#"

        def adjacentCells(indCell):
            i, j = indCell
            adjacent = set()
            for k in range(4):
                nextI, nextJ = i + directions[k], j + directions[k+1]
                if locationValid(nextI, nextJ): adjacent.add((nextI, nextJ))
            return adjacent

        def oppositeCell(box, cell):
            return (2 * box[0] - cell[0], 2 * box[1] - cell[1])

        def reachableByPerson(person, box):
            reachable = set()
            reachable.add(person)

            cellQueue = deque()
            cellQueue.appendleft(person)

            while cellQueue:
                thisCell = cellQueue.pop()
                for nextCell in adjacentCells(thisCell):
                    if nextCell != box and nextCell not in reachable:
                        reachable.add(nextCell)
                        cellQueue.appendleft(nextCell)

            return reachable

        def validMoves(person, box):
            reachable = reachableByPerson(person, box)
            adjacent = adjacentCells(box)
            moves = []

            for indCell in adjacent:
                boxTarget = oppositeCell(box, indCell)
                if indCell in reachable and boxTarget in adjacent:
                    moves.append((box, boxTarget))

            return moves

        findElements()
        stateQueue = deque()
        stateQueue.appendleft((person, box, 0))
        visitedStates = set()
        visitedStates.add((person, box))

        while stateQueue:
            currentPerson, currentBox, numMoves = stateQueue.pop()
            if currentBox == target:
                return numMoves
            nextStates = validMoves(currentPerson, currentBox)
            for nextPerson, nextBox in nextStates:
                if (nextPerson, nextBox) not in visitedStates:
                    visitedStates.add((nextPerson, nextBox))
                    stateQueue.appendleft((nextPerson, nextBox, numMoves + 1))

        return -1 
