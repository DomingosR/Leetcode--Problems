class Solution(object):
    def solve(self, board):
        m = len(board)
        n = len(board[0])
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        
        cellQueue = deque()

        def processCell(i, j):
            if board[i][j] == "O":
                board[i][j] = "M"
                for (deltaI, deltaJ) in directions:
                    nextI = i + deltaI
                    nextJ = j + deltaJ
                    if m > nextI >= 0 <= nextJ < n and board[nextI][nextJ] == "O":
                        cellQueue.appendleft([nextI, nextJ])

        for j in range(n):
            if board[0][j] == "O":
                cellQueue.appendleft([0, j])
            if board[m-1][j] == "O":
                cellQueue.appendleft([m-1, j])
        
        for i in range(1, m-1):
            if board[i][0] == "O":
                cellQueue.appendleft([i, 0])
            if board[i][n-1] == "O":
                cellQueue.appendleft([i, n-1])

        while cellQueue:
            i, j = cellQueue.pop()
            processCell(i, j)

        for i in range(m):
            for j in range(n):
                board[i][j] = "O" if board[i][j] == "M" else "X"