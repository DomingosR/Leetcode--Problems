class Solution(object):
    def numRookCaptures(self, board):
        # First, find rook on board
        rookRow, rookCol = 0, 0
        while board[rookRow][rookCol] != "R":
            if rookCol == 7:
                rookRow += 1
                rookCol = 0
            else:
                rookCol += 1

        # Search in every direction
        countPawns = 0

        directions = [0, 1, 0, -1, 0]
        for i in range(4):
            currRow, currCol = rookRow, rookCol
            dRow, dCol = directions[i:i+2]
            while 8 > currRow >= 0 <= currCol < 8:
                if board[currRow][currCol] == "p":
                    countPawns += 1
                    break
                if board[currRow][currCol] == "B":
                    break
                currRow += dRow
                currCol += dCol

        return countPawns
