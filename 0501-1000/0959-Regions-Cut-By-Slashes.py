class Solution(object):
    def regionsBySlashes(self, grid):
        n = len(grid)
        UFParent = list(range(4 * (n ** 2)))
        regionCount = [4 * (n ** 2)]
        
        def find(reg):
            if reg != UFParent[reg]:
                UFParent[reg] = find(UFParent[reg])
            return UFParent[reg]
        
        def union(reg1, reg2):
            reg1, reg2 = find(reg1), find(reg2)
            if reg1 != reg2:
                UFParent[reg2] = reg1
                regionCount[0] -= 1
                return True
            return False
        
        def startRegion(i, j):
            return 4 * (n * i + j)
        
        set1, set2 = set([" ", "/"]), set([" ", "\\"])
        
        for i in range(n):
            for j in range(n):
                currReg = startRegion(i, j)
                currVal = grid[i][j]
                
                if currVal in set1:
                    union(currReg, currReg + 3)
                    union(currReg + 1, currReg + 2)
                    
                if currVal in set2:
                    union(currReg, currReg + 1)
                    union(currReg + 2, currReg + 3)
                    
                if i < n-1:
                    belowReg = startRegion(i+1, j)
                    union(currReg + 2, belowReg)
                    
                if j < n-1:
                    rightReg = startRegion(i, j+1)
                    union(currReg + 1, rightReg + 3)
                    
        return regionCount[0]