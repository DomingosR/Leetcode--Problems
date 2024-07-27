class Solution(object):
    def updateMatrix(self, mat):
        m, n = len(mat), len(mat[0])
        directions = [0, 1, 0, -1, 0]

        cellQueue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    cellQueue.appendleft((i, j))
                else:
                    mat[i][j] = -1

        while cellQueue:
            i, j = cellQueue.pop()

            for k in range(4):
                nextRow, nextCol = i + directions[k], j + directions[k + 1]
                if nextRow < 0 or nextRow == m or nextCol < 0 or nextCol == n:
                    continue
                if mat[nextRow][nextCol] == -1:
                    mat[nextRow][nextCol] = mat[i][j] + 1
                    cellQueue.appendleft((nextRow, nextCol))

        return mat
