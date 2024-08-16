class Solution(object):
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return True
        
        def cellDirections(gridVal):
            if gridVal == 1: return {"L", "R"}
            if gridVal == 2: return {"T", "B"}
            if gridVal == 3: return {"L", "B"}
            if gridVal == 4: return {"R", "B"}
            if gridVal == 5: return {"T", "L"}
            if gridVal == 6: return {"T", "R"}
            
        def oppositeDirection(inputDir):
            if inputDir == "T": return "B"
            if inputDir == "B": return "T"
            if inputDir == "L": return "R"
            if inputDir == "R": return "L"
            
        def nextCell(i, j, outgoingDir):
            if outgoingDir == "T": cellVal = (i-1, j)
            if outgoingDir == "B": cellVal = (i+1, j)
            if outgoingDir == "L": cellVal = (i, j-1)
            if outgoingDir == "R": cellVal = (i, j+1)
            
            nextI, nextJ = cellVal
            
            if not (m > nextI >= 0 <= nextJ < n):
                return (-1, -1, "Dead End")
            
            nextCellDirections = cellDirections(grid[nextI][nextJ])
            incomingDir = oppositeDirection(outgoingDir)
            if incomingDir not in nextCellDirections:
                return (-1, -1, "Dead End")
                        
            if nextI == m-1 and nextJ == n-1:
                return (m-1, n-1, "Found")
            
            nextDirection = list(nextCellDirections - set([incomingDir]))[0]
            return (nextI, nextJ, nextDirection)
            
        for startDir in cellDirections(grid[0][0]):
            if startDir in {"B", "R"}:
                currentI, currentJ, currentDir = 0, 0, startDir
                visited = set([(0, 0)])
                while True:
                    currentI, currentJ, currentDir = nextCell(currentI, currentJ, currentDir)
                    if currentDir == "Found":
                        return True
                    if currentDir == "Dead End" or (currentI, currentJ) in visited:
                        break                    
                    visited.add((currentI, currentJ))
                    
        return False