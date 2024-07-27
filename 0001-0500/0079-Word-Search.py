class Solution(object):
    def exist(self, board, word):
        numRows = len(board)
        numCols = len(board[0])
        wordLen = len(word)

        if wordLen > numRows * numCols:
            return False

        letterCounterWord = Counter(word)
        letterCounterBoard = Counter(chain(*board))
        if not (letterCounterWord <= letterCounterBoard):
            return False

        if letterCounterWord[word[0]] > letterCounterWord[word[-1]]:
             word = word[::-1]

        def dfs(i, j, s):
            if s == wordLen:
                return True
            if (numRows > i >= 0 <= j < numCols) and board[i][j] == word[s]:
                board[i][j] = "!"
                nextCells = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                retVal = any(dfs(nextI, nextJ, s+1) for (nextI, nextJ) in nextCells)
                board[i][j] = word[s]
                return retVal
            else:
                return False

        return any(dfs(i, j, 0) for i, j in product(range(numRows), range(numCols)))
