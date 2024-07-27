class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board)
        visited = [0] * (n**2)

        def squareToRC(square):
            aux1 = (square - 1) // n
            aux2 = (square - 1) % n
            r = (n-1) - aux1
            c = aux2 if aux1 % 2 == 0 else (n-1)-aux2
            return (r, c)

        cellQueue = deque()
        cellQueue.append([1, 0])
        visited[0] = 1

        while cellQueue:
            currentNum, level = cellQueue.pop()
            for i in range(6):
                nextNum = currentNum + i + 1
                r, c = squareToRC(nextNum)
                if board[r][c] != -1:
                    nextNum = board[r][c]
                if nextNum == n**2:
                    return level + 1

                if visited[nextNum-1] == 0:
                    cellQueue.appendleft([nextNum, level+1])
                    visited[nextNum-1] = 1

        return -1
