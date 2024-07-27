def makeMove(board, i, j):
    minIndex = min(i, j)
    minChar = board[minIndex:minIndex + 1]
    maxIndex = max(i, j)
    maxChar = board[maxIndex:maxIndex + 1]
    finalStr = board[:minIndex] + maxChar + board[minIndex+1:maxIndex] + minChar + board[maxIndex+1:]

    return finalStr

def minMoves(initialBoard):
    # Iteration parameters
    answerBoard = "123450"
    validMoves = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

    # Convert board to string
    currentBoard = ""
    for i in range(2):
        for j in range(3):
            currentBoard += str(initialBoard[i][j])

    # Initialize search
    boardsConsidered = [currentBoard]
    minMovesPerBoard = [0]
    boardIndex = 0
    
    # First, check if initial board is the solution
    if currentBoard == answerBoard:
        return 0

    # Perform search
    while boardIndex < len(boardsConsidered):
        currentBoard = boardsConsidered[boardIndex]
        currentNumMoves = minMovesPerBoard[boardIndex]
        zeroPosition = currentBoard.index("0")
        possibleMoves = validMoves[zeroPosition]

        for move in possibleMoves:
            newBoard = makeMove(currentBoard, zeroPosition, move)
            if newBoard == answerBoard:
                return currentNumMoves + 1

            elif newBoard not in boardsConsidered:
                boardsConsidered.append(newBoard)
                minMovesPerBoard.append(currentNumMoves + 1)

        boardIndex += 1

    return -1
    
class Solution(object):
    def slidingPuzzle(self, board):
        return minMoves(board)