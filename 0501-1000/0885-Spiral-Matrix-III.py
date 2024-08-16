class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        totalCells = rows * cols - 1
        positions = [[rStart, cStart]]
        currentRow, currentCol = rStart, cStart
        directions = [0, 1, 0, -1, 0]
        currentDir, numSteps = 3, 1

        while totalCells > 0:
            for _ in range(2):
                currentDir = (currentDir + 1) % 4
                dRow, dCol = directions[currentDir], directions[currentDir + 1]
                for i in range(numSteps):
                    currentRow, currentCol = currentRow + dRow, currentCol + dCol
                    if rows > currentRow >= 0 <= currentCol < cols:
                        positions.append([currentRow, currentCol])
                        totalCells -= 1

            numSteps += 1

        return positions