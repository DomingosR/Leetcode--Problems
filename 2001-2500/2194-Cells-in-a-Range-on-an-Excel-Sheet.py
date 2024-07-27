class Solution(object):
    def cellsInRange(self, s):
        listOfCells = []

        initialCell = s[:2]
        initialCol = initialCell[0]
        initialRow = int(initialCell[-1])

        finalCell = s[-2:]
        finalCol = finalCell[0]
        finalRow = int(finalCell[-1])

        currentCell = initialCell
        listOfCells.append(currentCell)

        while currentCell != finalCell:
            currentCol = currentCell[0]
            currentRow = int(currentCell[-1])

            if currentRow == finalRow:
                nextRow = initialRow
                nextCol = chr(ord(currentCol) + 1)
            else:
                nextRow = currentRow + 1
                nextCol = currentCol

            currentCell = nextCol + str(nextRow)
            listOfCells.append(currentCell)

        return listOfCells
