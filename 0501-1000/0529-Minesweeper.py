class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])
        directions = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}
        processed = [[0] * n for _ in range(m)]

        def numAdjacentMines(i, j):
            mineCount = 0
            for dI, dJ in directions:
                i1, j1 = i + dI, j + dJ
                if m > i1 >= 0 <= j1 < n:
                    mineCount += (1 if board[i1][j1] == "M" else 0)
            return mineCount

        i, j = click

        if board[i][j] == "M":
            board[i][j] = "X"
            return board

        def processCell(i1, j1):
            if processed[i1][j1] == 0:
                processed[i1][j1] = 1
                if board[i1][j1] == "E":
                    countMines = numAdjacentMines(i1, j1)
                    if countMines > 0:
                        board[i1][j1] = str(countMines)
                    else:
                        board[i1][j1] = "B"
                        for dI, dJ in directions:
                            i2, j2 = i1 + dI, j1 + dJ
                            if m > i2 >= 0 <= j2 < n:
                                processCell(i2, j2)

        processCell(i, j)
        return board
