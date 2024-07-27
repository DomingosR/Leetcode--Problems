def permutationToBoard(boardVal, n):
    mainArray = []

    for i in range(n):
        currentPos = boardVal[i].index(1)
        currentStr = "." * currentPos + "Q" + "." * (n - currentPos - 1)
        mainArray.append(currentStr)

    return mainArray

def markAttackedSquares(boardVal, queenRow, queenCol, n):
    auxInt = max(n - queenRow - 1, n - queenCol - 1, queenCol)

    for j in range(1, auxInt + 1):

        # Squares directly below target square
        if queenRow + j <= n-1 and boardVal[queenRow + j][queenCol] == 0:
            boardVal[queenRow + j][queenCol] = -(queenRow+1)

        if queenCol - j >= 0:
            # Squares to the left of target square
            if boardVal[queenRow][queenCol - j] == 0:
                boardVal[queenRow][queenCol - j] = -(queenRow+1)

            # Squares on diagonal down and to the left of target square
            if queenRow + j <= (n-1) and boardVal[queenRow + j][queenCol - j] == 0:
                boardVal[queenRow + j][queenCol - j] = -(queenRow+1)

        if queenCol + j <= (n-1):
            # Squares to the right of target square
            if boardVal[queenRow][queenCol + j] == 0:
                boardVal[queenRow][queenCol + j] = -(queenRow+1)

            # Squares on diagonal down and to the right of target square
            if queenRow + j <= (n-1) and boardVal[queenRow + j][queenCol + j] == 0:
                boardVal[queenRow + j][queenCol + j] = -(queenRow+1)

    return boardVal

def backtrack(currentRow, boardVal, n):
    currentRow -= 1
    iterationFinished = 0

    while iterationFinished == 0:
        queenPos = boardVal[currentRow].index(1)
        boardVal[currentRow][queenPos] = 0

        for j in range(currentRow, n):
            for k in range(n):
                if boardVal[j][k] == -(currentRow+1):
                    boardVal[j][k] = 0

        if queenPos < n-1 and (0 in boardVal[currentRow][queenPos+1:]):
            # Found a square for a queen in this row, so we're done backtracking
            # and need only process this row
            newQueenPos = queenPos + boardVal[currentRow][queenPos+1:].index(0) + 1
            boardVal[currentRow][newQueenPos] = 1

            # Mark squares attacked by this newly placed queen
            boardVal = markAttackedSquares(boardVal, currentRow, newQueenPos, n)

            # Increment current row and iterate
            currentRow += 1
            iterationFinished = 1

        else:
            # Could not find a square for the queen, so move up one row
            currentRow -= 1
            if currentRow == -1:
                iterationFinished = 1

    return boardVal, currentRow

def nQueensSolutionV2(n):
    # *** Variables to hold return information
    validPositions = []

    # *** Arrays to keep track of information during the loop ***
    # This array will contain most of the needed information for the main
    # algorithm.  The values of the cells are:
    #  0 : if the cell is empty and not attacked by a queen
    #  1 : if the cell is occupied by a queen
    #  -i: if the cell is empty, but attacked by the queen in row (i-1)
    #      (so this ranges from -1 to -n)
    boardVal = [[0 for i in range(n)] for j in range(n)]

    # The following variable contains the next row to be explorer
    currentRow = 0

    # *** Main iteration loop ***
    while currentRow >= 0:
        # First, check if a solution was found
        if currentRow == n:
            validPositions.append(permutationToBoard(boardVal, n))
            boardVal, currentRow = backtrack(currentRow, boardVal, n)

        # Then, search for a 0 (permissible queen square) in the current row
        elif 0 in boardVal[currentRow]:
            # There is an open square for the queen, so place it there and iterate
            currentCol = boardVal[currentRow].index(0)
            boardVal[currentRow][currentCol] = 1

            # Mark squares attacked by this newly placed queen
            boardVal = markAttackedSquares(boardVal, currentRow, currentCol, n)

            # Increment current row and recurse
            currentRow += 1

        else:
            # There are no open squares for the queen in current row, so back up
            # until we find a valid open space to the right of the current queen in the
            # next row above
            boardVal, currentRow = backtrack(currentRow, boardVal, n)

    return validPositions
    
class Solution(object):
    def solveNQueens(self, n):
        return nQueensSolutionV2(n)