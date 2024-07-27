class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)
        rowDict = defaultdict(int)
        colDict = defaultdict(int)
        
        for i in range(n):
            rowStr = "-".join([str(grid[i][j]) for j in range(n)])
            colStr = "-".join([str(grid[j][i]) for j in range(n)])
            rowDict[rowStr] += 1
            colDict[colStr] += 1
            
        numPairs = 0
        
        for rowStr in rowDict:
            numPairs += rowDict[rowStr] * colDict[rowStr]
        
        return numPairs