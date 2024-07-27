class Solution(object):
    def cherryPickup(self, grid):
        m, n = len(grid), len(grid[0])

        previousValues = defaultdict(int)

        def numCherries(row, col1, col2):
            if (row, col1, col2) in previousValues:
                return previousValues[(row, col1, col2)]

            if col1 == col2:
                currentVal = grid[row][col1]
            else:
                currentVal = grid[row][col1] + grid[row][col2]
            
            if row == m-1:
                previousValues[(row, col1, col2)] = currentVal
                return currentVal
            
            overallVal = currentVal
            for nextCol1 in range(max(0, col1 - 1), min(n, col1 + 2)):
                for nextCol2 in range(max(0, col2 - 1), min(n, col2 + 2)):
                    overallVal = max(overallVal, currentVal + numCherries(row + 1, nextCol1, nextCol2))
            
            previousValues[(row, col1, col2)] = overallVal
            return overallVal

        return numCherries(0, 0, n-1)