class Solution(object):
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        
        def nextState(i, j):
            startRow, endRow = max(i-1, 0), min(i+1, m-1)
            startCol, endCol = max(j-1, 0), min(j+1, n-1)
            
            totalSum = - board[i][j]
            
            for i1 in range(startRow, endRow + 1):
                for j1 in range(startCol, endCol + 1):
                    totalSum += (board[i1][j1] & 1)
                    
            finalState = 0
            if totalSum == 3 or (totalSum == 2 and (board[i][j] & 1)):
                finalState = 1
            
            return finalState
                                 
        for i in range(m):
            for j in range(n):
                board[i][j] |= (nextState(i, j) << 1)
                                 
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
                                 
        return board