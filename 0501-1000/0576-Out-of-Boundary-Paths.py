def countNumPaths(m, n, maxMove, startRow, startColumn):
    if maxMove == 0:
        return 0
    
    p = 10**9 + 7
    totalPaths = 0
    currentCount = [[0 for j in range(n)] for i in range(m)]
    currentCount[startRow][startColumn] = 1
    nextCount = [[0 for j in range(n)] for i in range(m)]
    nMoves = 0
    
    def processCell(i, j, moveNo):
        nonlocal totalPaths
        nextVal = 0
        if i == 0:
            totalPaths += currentCount[i][j]
        else:
            nextVal += currentCount[i-1][j]
        
        if i == m-1:
            totalPaths += currentCount[i][j]
        else:
            nextVal += currentCount[i+1][j]
        
        if j == 0:
            totalPaths += currentCount[i][j]
        else:
            nextVal += currentCount[i][j-1]
        
        if j == n-1:
            totalPaths += currentCount[i][j]
        else:
            nextVal += currentCount[i][j+1]
   
        nextCount[i][j] = nextVal
        totalPaths = totalPaths % p
            
    while nMoves < maxMove:
        for i in range(m):
            for j in range(n):
                processCell(i, j, nMoves + 1)
        
        currentCount = nextCount
        nextCount = [[0 for j in range(n)] for i in range(m)]
        nMoves += 1
        
    return totalPaths

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        return countNumPaths(m, n, maxMove, startRow, startColumn)