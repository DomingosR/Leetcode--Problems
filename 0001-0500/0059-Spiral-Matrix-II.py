class Solution(object):
    def generateMatrix(self, n):
        spiral = [[0] * n for _ in range(n)]
        i, j, count = 0, 0, 0
        di, dj = 0, 1

        while count < n**2:
            spiral[i][j] = count + 1
            if spiral[(i + di) % n][(j + dj) % n] > 0:
                di, dj = dj, -di
            i += di
            j += dj
            count += 1

        return spiral
