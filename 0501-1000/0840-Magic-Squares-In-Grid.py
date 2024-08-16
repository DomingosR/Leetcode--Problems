class Solution(object):
    def numMagicSquaresInside(self, grid):
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        
        def isMagic(i, j):
            allNums = set([grid[i1][j1] for i1 in range(i, i+3) for j1 in range(j, j+3)])
            if len(allNums) < 9 or max(allNums) > 9 or min(allNums) < 1:
                return False
            
            tempGrid = [grid[i1][j:j+3] for i1 in range(i, i+3)]
            if tempGrid[1][1] != 5:
                return False
            
            rowSums = set([sum(tempGrid[i]) for i in range(3)])
            if len(rowSums) > 1 or 15 not in rowSums:
                return False
            
            tempGridT = list(map(list, zip(*tempGrid)))
            colSums = set([sum(tempGridT[i]) for i in range(3)])
            if len(colSums) > 1 or 15 not in rowSums:
                return False
            
            diagSums = set()
            diagSums.add(tempGrid[0][0] + tempGrid[1][1] + tempGrid[2][2])
            diagSums.add(tempGrid[0][2] + tempGrid[1][1] + tempGrid[2][0])
            if len(diagSums) > 1 or 15 not in diagSums:
                return False
            
            return True
                
        return sum([isMagic(i, j) for i in range(len(grid) - 2) for j in range(len(grid[0]) - 2)])