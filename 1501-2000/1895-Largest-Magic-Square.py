class Solution(object):
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])
        
        rowSums = [[0] * (n+2) for _ in range(m+1)]
        colSums = [[0] * (n+2) for _ in range(m+1)]
        diagSums = [[0] * (n+2) for _ in range(m+1)]
        antiDiagSums = [[0] * (n+2) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                rowSums[i+1][j+1] = rowSums[i+1][j] + grid[i][j]
                colSums[i+1][j+1] = colSums[i][j+1] + grid[i][j]
                diagSums[i+1][j+1] = diagSums[i][j] + grid[i][j]
                antiDiagSums[i+1][j+1] = antiDiagSums[i][j+2] + grid[i][j]
        
        maxSize = min(m, n)
        k = maxSize
        
        while k > 1:
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    diagSum1 = diagSums[i+k][j+k] - diagSums[i][j]
                    diagSum2 = antiDiagSums[i+k][j+1] - antiDiagSums[i][j+k+1]
                        
                    if not diagSum1 == diagSum2:
                        continue

                    squareRowSums = [(rowSums[i1][j+k] - rowSums[i1][j]) for i1 in range(i+1, i+k+1)]
                    if (len(set(squareRowSums)) > 1) or (diagSum1 not in squareRowSums):
                         continue
                    
                    squareColSums = [colSums[i+k][j1] - colSums[i][j1] for j1 in range(j+1, j+k+1)]
                    if (len(set(squareColSums)) > 1) or (diagSum1 not in squareColSums):
                         continue                    

                    return k
                    
            k -= 1
            
        return 1