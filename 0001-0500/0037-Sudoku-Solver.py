class Solution(object):
    def solveSudoku(self, board):
        def validDigits(row, col):
            allDigits = "123456789"
            transposeBoard = list(map(list, zip(*board)))
            startRow, startCol = 3 * (row // 3), 3 * (col // 3)
            currentBlock = [board[startRow + i][startCol + j] for i in range(3) for j in range(3)]
            return set(allDigits) - set(board[row] + transposeBoard[col] + currentBlock + ["."])

        def solve(i):
            if i == 81:
                return True
            row, col = i // 9, i % 9
            if board[row][col] == ".":
                for digit in validDigits(row, col):
                    board[row][col] = digit
                    if solve(i+1):
                        return True
                    board[row][col] = "."
            else:
                if solve(i+1):
                    return True
            return False
        
        solve(0)